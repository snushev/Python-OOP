from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class StandardInfluencer(BaseInfluencer):
    INITIAL_PAYMENT_PERCENTAGE = 0.45

    def calculate_payment(self, campaign: BaseCampaign):
        return campaign.budget * self.INITIAL_PAYMENT_PERCENTAGE

    def reached_followers(self, campaign_type: str):
        followers = 0
        if campaign_type == "HighBudgetCampaign":
            followers = self.followers * self.engagement_rate * 1.2
        elif campaign_type == "LowBudgetCampaign":
            followers = self.followers * self.engagement_rate * 0.9
        return int(followers)