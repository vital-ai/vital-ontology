
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyGroupInstanceSummary(VITAL_Node):
        haleyGroupInstanceStatus: str
        numberOfAnsweredInvalidQuestions: int
        numberOfAnsweredPendingQuestions: int
        numberOfAnsweredQuestions: int
        numberOfAnsweredRequiredQuestions: int
        numberOfPendingQuestions: int
        numberOfQuestions: int
        numberOfRequiredQuestions: int

