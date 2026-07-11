
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyChatAuthenticationEvent(VITAL_Node):
        authenticationDateTime: datetime
        authenticationEventStatusURI: str
        accountURI: str
        loginURI: str

