
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyMindQueryAnswerBinding(VITAL_Node):
        answerBindingVariable: str
        binaryAnswerBinding: str
        booleanAnswerBinding: bool
        dateTimeAnswerBinding: datetime
        doubleAnswerBinding: float
        integerAnswerBinding: int
        listBinaryAnswerBinding: str
        listBooleanAnswerBinding: bool
        listDateTimeAnswerBinding: datetime
        listDoubleAnswerBinding: float
        listIntegerAnswerBinding: int
        listStringAnswerBinding: str
        listURIAnswerBinding: str
        stringAnswerBinding: str
        uRIAnswerBinding: str

