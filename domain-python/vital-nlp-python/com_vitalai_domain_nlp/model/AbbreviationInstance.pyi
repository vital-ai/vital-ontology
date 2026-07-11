
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class AbbreviationInstance(VITAL_Node):
        longForm: str
        longFormEnd: int
        longFormStart: int
        shortForm: str
        shortFormEnd: int
        shortFormStart: int

