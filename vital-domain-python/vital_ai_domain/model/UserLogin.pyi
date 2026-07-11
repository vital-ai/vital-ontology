
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class UserLogin(VITAL_Node):
        emailAddress: str
        verificationCode: str
        emailVerified: bool
        locked: bool

