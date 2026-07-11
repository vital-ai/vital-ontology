
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class EndpointProfile(VITAL_Node):
        locale: str
        authLoginProfile: bool
        premium: bool

