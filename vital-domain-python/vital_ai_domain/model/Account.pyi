
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class Account(VITAL_Node):
        accountID: str
        accountLoginSuffix: str
        localLoginsType: str
        localLoginsValidated: bool
        locked: bool
        retired: bool

