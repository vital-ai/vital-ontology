
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class NlpEntity(VITAL_Node):
        extractSource: str
        nlpEntityCategory: str
        relevance: float
        wikipediaURL: str

