
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class FeatureValue(VITAL_Node):
        featureKey: str
        featureStringValue: str
        featureType: str
        featureURIValue: str
        featureWeight: float

