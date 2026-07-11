
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyAnswerType(VITAL_Node):
        answerTypeExernalVersion: str
        answerTypeExternalIdentifier: str
        answerTypeExternalName: str
        answerTypeIdentifier: str
        answerTypeUseEndDate: datetime
        answerTypeUseStartDate: datetime
        answerTypeVersion: str
        haleyAnswerDataType: str
        haleyAnswerTypeCategory: str
        haleyAnswerUnitType: str
        haleyCurrencyType: str
        activeAnswerType: bool
        rootAnswerType: bool
        description: str

