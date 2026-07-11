
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class AgentStatusResponse(VITAL_Node):
        id: str
        json: str
        requestURI: str
        sourceRequestURI: str
        status: str
        statusMessage: str

