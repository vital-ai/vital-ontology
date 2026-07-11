
import datetime
from com_vitalai_domain_social.model.SocialMediaAccount import SocialMediaAccount


class InstagramAccount(SocialMediaAccount):
        bio: str
        followersCount: int
        followingCount: int
        instagramID: str
        mediaCount: int
        socialUsername: str
        website: str

