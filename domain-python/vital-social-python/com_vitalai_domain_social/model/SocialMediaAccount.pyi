
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class SocialMediaAccount(VITAL_Node):
        accessToken: str
        pictureURL: str
        socialLikeCount: int
        tokenValid: bool

