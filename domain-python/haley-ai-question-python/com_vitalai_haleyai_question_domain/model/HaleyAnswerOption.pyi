
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyAnswerOption(VITAL_Node):
        answerSetMemberURI: str
        optionImageURL: str
        optionLargeImageURL: str
        optionMediumImageURL: str
        optionName: str
        optionOrder: int
        optionSmallImageURL: str
        optionURL: str
        optionValue: str
        suppressedAnswerOption: bool

