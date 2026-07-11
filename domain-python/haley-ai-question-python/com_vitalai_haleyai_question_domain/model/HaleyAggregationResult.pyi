
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyAggregationResult(VITAL_Node):
        aggregationDoubleValue: float
        aggregationIntegerValue: int
        aggregationName: str
        aggregationType: str

