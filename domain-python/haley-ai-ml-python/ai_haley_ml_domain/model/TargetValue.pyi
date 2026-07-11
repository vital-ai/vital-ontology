
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class TargetValue(VITAL_Node):
        targetBooleanValue: bool
        targetDoubleValue: float
        targetEncodedStringValue: str
        targetIntegerValue: int
        targetKey: str
        targetStringValue: str
        targetType: str
        targetURIValue: str
        targetWeight: float

