
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyAccessGrant(VITAL_Node):
        haleyAccessRightURI: str
        roleGrantAspectURI: str
        roleGrantExtentURI: str
        roleGrantTypeURI: str
        accountURI: str
        loginURI: str

