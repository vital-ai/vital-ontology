
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyAnswerOptionLongDependency(VITAL_Node):
        booleanAnswerValue: bool
        choiceAnswerValue: str
        dateTimeAnswerValue: datetime
        doubleAnswerValue: float
        fileAnswerValueURI: str
        integerAnswerValue: int
        longTextAnswerValue: str
        multiChoiceAnswerValue: str
        multiTaxonomyAnswerValue: str
        objectAnswerValueURI: str
        taxonomyAnswerValue: str
        textAnswerValue: str

