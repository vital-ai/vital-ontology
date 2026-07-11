
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyRegion(VITAL_Node):
        centroidLatitude: float
        centroidLongitude: float
        recentRegionPopulation: int
        recentRegionPopulationYear: int

