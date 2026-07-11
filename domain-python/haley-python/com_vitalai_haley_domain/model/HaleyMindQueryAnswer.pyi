
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyMindQueryAnswer(VITAL_Node):
        answerToRuleURI: str
        haleyMindAnswerDerivationTree: str
        haleyMindAnswerExplanation: str
        haleyMindQueryAnswerResult: bool

