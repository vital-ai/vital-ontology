
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyQuery(VITAL_Node):
        haleyQueryJSON: str
        haleyQueryName: str
        haleyQueryAggregationOnlyRequest: bool
        haleyQueryContainerRequest: bool

