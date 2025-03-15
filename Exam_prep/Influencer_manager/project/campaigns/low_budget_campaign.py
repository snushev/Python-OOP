from project.campaigns.base_campaign import BaseCampaign


class LowBudgetCampaign(BaseCampaign):
    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id=campaign_id, brand=brand, required_engagement=required_engagement, budget=2500)


    def check_eligibility(self, engagement_rate: float):
        if engagement_rate >= self.required_engagement * 0.9:
            return True
        return False