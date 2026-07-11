
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class AgentDatascriptCallRequest(VITAL_Node):
        accountURI: str
        datascriptScope: str
        id: str
        json: str
        scriptName: str
        threadURI: str

