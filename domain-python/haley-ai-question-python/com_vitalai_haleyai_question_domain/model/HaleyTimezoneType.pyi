
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyTimezoneType(VITAL_Node):
        daylightSavingsTimeUTCType: str
        standardTimeUTCType: str
        daylightSavingsZone: bool

