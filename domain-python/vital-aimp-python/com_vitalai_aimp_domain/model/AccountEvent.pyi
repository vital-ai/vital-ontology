
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class AccountEvent(VITAL_Node):
        accountURI: str
        accountEventAccountURI: str
        accountEventDateTime: datetime
        accountEventIdentifier: str
        accountEventLoginURI: str
        accountEventTypeURI: str

