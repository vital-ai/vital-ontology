
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyPredictionModel(VITAL_Node):
        modelIdentifier: str
        predictionImplementingClass: str
        predictionModelClassURI: str
        predictionModelEndpoint: str
        predictionModelProvider: str
        predictionModelStructureType: str
        predictionModelType: str
        version: str
        globalPredictionModel: bool

