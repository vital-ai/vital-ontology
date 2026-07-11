
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyGroup(VITAL_Node):
        defaultPrecedence: int
        groupIndex: int
        haleyGroupBase: str
        haleyGroupBaseVersion: str
        haleyGroupNatureTypeURI: str
        haleyGroupTypeURI: str

