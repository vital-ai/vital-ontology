
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class AgentDatascriptCallResponse(VITAL_Node):
        accountURI: str
        bindingNames: str
        datascriptScope: str
        id: str
        limit: int
        offset: int
        requestURI: str
        scriptName: str
        sourceRequestURI: str
        status: str
        statusMessage: str
        threadURI: str
        totalResults: int

