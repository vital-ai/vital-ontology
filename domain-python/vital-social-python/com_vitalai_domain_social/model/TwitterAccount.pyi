
import datetime
from com_vitalai_domain_social.model.SocialMediaAccount import SocialMediaAccount


class TwitterAccount(SocialMediaAccount):
        followersCount: int
        followingCount: int
        oAuthTokenSecret: str
        screenName: str
        socialDescription: str
        tweetsCount: int
        twitterID: int
        twitterOAuthToken: str

