
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class NlpEntityInstance(VITAL_Node):
        entityAuthor: str
        entityOffset: int
        entityOffsetInSentence: int
        exactString: str
        length: int
        lengthInSentence: int
        sentimentScore: float
        spanType: str
        sentimentMixed: bool

