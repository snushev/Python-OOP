from project.artifacts.base_artifact import BaseArtifact
from project.artifacts.contemporary_artifact import ContemporaryArtifact
from project.artifacts.renaissance_artifact import RenaissanceArtifact
from project.collectors.base_collector import BaseCollector
from project.collectors.museum import Museum
from project.collectors.private_collector import PrivateCollector


class AuctionHouseManagerApp:
    def __init__(self):
        self.artifacts: list[BaseArtifact] = []
        self.collectors: list[BaseCollector] = []

    def register_artifact(self, artifact_type: str, artifact_name: str, artifact_price: float, artifact_space: int):
        valid_artifacts = ["RenaissanceArtifact", "ContemporaryArtifact"]
        if artifact_type not in valid_artifacts:
            raise ValueError("Unknown artifact type!")
        elif [x.name for x in self.artifacts if x.name == artifact_name]:
            raise ValueError(f"{artifact_name} has been already registered!")
        elif artifact_type == valid_artifacts[0]:
            self.artifacts.append(RenaissanceArtifact(artifact_name, artifact_price, artifact_space))
        elif artifact_type == valid_artifacts[1]:
            self.artifacts.append(ContemporaryArtifact(artifact_name, artifact_price, artifact_space))
        return f"{artifact_name} is successfully added to the auction as {artifact_type}."

    def register_collector(self, collector_type: str, collector_name: str):
        valid_collectors = ["Museum", "PrivateCollector"]
        if collector_type not in valid_collectors:
            raise ValueError("Unknown collector type!")
        elif [x.name for x in self.collectors if x.name == collector_name]:
            raise ValueError(f"{collector_name} has been already registered!")
        elif collector_type == valid_collectors[0]:
            self.collectors.append(Museum(collector_name))
        elif collector_type == valid_collectors[1]:
            self.collectors.append(PrivateCollector(collector_name))
        return f"{collector_name} is successfully registered as a {collector_type}."

    def perform_purchase(self, collector_name: str, artifact_name: str):
        collector = next((x for x in self.collectors if x.name == collector_name), None)
        if collector is None:
            raise ValueError(f"Collector {collector_name} is not registered to the auction!")
        artifact = next((x for x in self.artifacts if x.name == artifact_name), None)
        if artifact is None:
            raise ValueError(f"Artifact {artifact_name} is not registered to the auction!")
        if not collector.can_purchase(artifact.price, artifact.space_required):
            return "Purchase is impossible."
        # Collector buys the artifact
        self.artifacts.remove(artifact)
        collector.purchased_artifacts.append(artifact)
        collector.available_money -= artifact.price
        collector.available_space -= artifact.space_required
        return f"{collector_name} purchased {artifact_name} for a price of {artifact.price:.2f}."

    def remove_artifact(self, artifact_name: str):
        artifact = next((x for x in self.artifacts if x.name == artifact_name), None)
        if artifact is None:
            return "No such artifact."
        self.artifacts.remove(artifact)
        return f"Removed {artifact.artifact_information()}"

    def fundraising_campaigns(self, max_money: float):
        counter = 0
        for collector in self.collectors:
            if collector.available_money <= max_money:
                collector.increase_money()
                counter += 1
        return f"{counter} collector/s increased their available money."

    def get_auction_report(self):
        sorted_collectors = sorted(self.collectors, key=lambda x: (-len(x.purchased_artifacts), x.name))
        count_of_sold_artifacts = sum([len(x.purchased_artifacts) for x in self.collectors])
        result = ["**Auction statistics**", f"Total number of sold artifacts: {count_of_sold_artifacts}", f"Available artifacts for sale: {len(self.artifacts)}", "***"]
        for collector in sorted_collectors:
            result.append(collector.__str__())
        return "\n".join(result)