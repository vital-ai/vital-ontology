
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class LoginDataEvent(VITAL_Node):
        loginURI: str
        entityURI: str
        eventType: str

