from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    def __init__(self):
        self.influencers: list[BaseInfluencer] = []
        self.campaigns: list[BaseCampaign] = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        valid_influencers = {
            "PremiumInfluencer": PremiumInfluencer,
            "StandardInfluencer": StandardInfluencer
        }

        if influencer_type not in valid_influencers:
            return f"{influencer_type} is not an allowed influencer type."
        if any(inf for inf in self.influencers if inf.username == username):
            return f"{username} is already registered."

        influencer_class = valid_influencers[influencer_type]
        self.influencers.append(influencer_class(username, followers, engagement_rate))
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        valid_campaigns = {
            "HighBudgetCampaign": HighBudgetCampaign,
            "LowBudgetCampaign": LowBudgetCampaign
        }

        if campaign_type not in valid_campaigns:
            return f"{campaign_type} is not a valid campaign type."
        if any(c for c in self.campaigns if c.campaign_id == campaign_id):
            return f"Campaign ID {campaign_id} has already been created."

        campaign_class = valid_campaigns[campaign_type]
        self.campaigns.append(campaign_class(campaign_id, brand, required_engagement))
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        influencer = next((i for i in self.influencers if i.username == influencer_username), None)
        if influencer is None:
            return f"Influencer '{influencer_username}' not found."

        campaign = next((c for c in self.campaigns if c.campaign_id == campaign_id), None)
        if campaign is None:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."

        calculated_payment = influencer.calculate_payment(campaign)
        if calculated_payment > 0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= calculated_payment
            influencer.campaigns_participated.append(campaign)
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."
    def calculate_total_reached_followers(self):
        total_followers = []
        for campaign in self.campaigns:
            total = 0
            if campaign.approved_influencers:
                for influencer in campaign.approved_influencers:
                    total += influencer.reached_followers(campaign.__class__.__name__)
            total_followers.append(total)
        return dict(zip(self.campaigns, total_followers))

    def influencer_campaign_report(self, username: str):
        influencer = next((i for i in self.influencers if i.username == username), None)
        if not influencer.campaigns_participated:
            return f"{username} has not participated in any campaigns."
        return influencer.display_campaigns_participated()

    def campaign_statistics(self):
        total_reached_followers_dict = self.calculate_total_reached_followers()

        sorted_campaigns = sorted(self.campaigns, key=lambda x: (len(x.approved_influencers), -x.budget))
        result = ["$$ Campaign Statistics $$", ]
        for campaign in sorted_campaigns:
            total_reached_followers = total_reached_followers_dict.get(campaign)
            result.append(f"  * Brand: {campaign.brand}, Total influencers: {len(campaign.approved_influencers)}, Total budget: ${campaign.budget:.2f}, Total reached followers: {total_reached_followers}")
        return '\n'.join(result)