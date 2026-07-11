
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyAnswer(VITAL_Node):
        aggregationRowURI: str
        aggregationType: str
        aggregrationQuestionURI: str
        haleyAnswerDataType: str
        haleyAnswerType: str
        haleyAnswerUnitType: str
        haleyMappedAnswerType: str
        preferredSelectorType: str
        aggregationAnswer: bool
        calculatedAnswerValue: bool
        dynamicRequiredAnswer: bool
        readOnlyAnswerValue: bool
        subjectToConstraints: bool
        subjectToValidation: bool

