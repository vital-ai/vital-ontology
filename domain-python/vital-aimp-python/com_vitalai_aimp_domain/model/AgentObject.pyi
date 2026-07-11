
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class AgentObject(VITAL_Node):
        accountURI: str
        loginURI: str
        channelURI: str
        requestURI: str
        sourceRequestURI: str
        sessionID: str

