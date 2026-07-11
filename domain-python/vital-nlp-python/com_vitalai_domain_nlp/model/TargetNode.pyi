
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class TargetNode(VITAL_Node):
        modelURI: str
        targetDoubleValue: float
        targetScore: float
        targetStringValue: str

