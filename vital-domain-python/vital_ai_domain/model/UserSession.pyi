
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class UserSession(VITAL_Node):
        expirationDate: datetime
        loginURI: str
        sessionID: str
        sessionType: str

