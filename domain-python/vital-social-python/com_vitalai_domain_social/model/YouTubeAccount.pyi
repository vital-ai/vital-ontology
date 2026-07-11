
import datetime
from com_vitalai_domain_social.model.SocialMediaAccount import SocialMediaAccount


class YouTubeAccount(SocialMediaAccount):
        channelID: str
        commentCount: int
        country: str
        expiresIn: int
        publishedAt: datetime
        refreshToken: str
        socialDescription: str
        subscriberCount: int
        videoCount: int
        viewCount: int

