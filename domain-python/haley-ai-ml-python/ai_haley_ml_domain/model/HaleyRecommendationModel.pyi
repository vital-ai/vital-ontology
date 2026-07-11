
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyRecommendationModel(VITAL_Node):
        modelIdentifier: str
        recommendationImplementingClass: str
        recommendationModelEndpoint: str
        recommendationModelStructureType: str
        recommendationModelType: str
        version: str
        globalRecommendationModel: bool

