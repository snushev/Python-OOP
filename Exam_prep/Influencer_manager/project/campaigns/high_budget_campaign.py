from project.campaigns.base_campaign import BaseCampaign


class HighBudgetCampaign(BaseCampaign):
    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id=campaign_id, brand=brand, required_engagement=required_engagement, budget=5000)


    def check_eligibility(self, engagement_rate: float):
        if engagement_rate >= self.required_engagement * 1.2:
            return True
        return False