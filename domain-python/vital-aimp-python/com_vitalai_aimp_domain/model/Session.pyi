
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class Session(VITAL_Node):
        authSessionID: str
        botID: str
        chatMode: str
        lastLeftAppMessageTime: int
        userID: str
        sessionID: str

