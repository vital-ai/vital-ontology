
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class Sentence(VITAL_Node):
        endPosition: int
        posTagsConfidenceString: str
        posTagsValuesString: str
        sentenceNumber: int
        startPosition: int
        tokensPositionsString: str
        tokensTextString: str

