
import datetime
from com_vitalai_haleyai_question_domain.model.HaleyAnswerInstance import HaleyAnswerInstance


class HaleyNumberAnswerInstance(HaleyAnswerInstance):
        doubleAnswerValue: float
        haleyAnswerSignificantDigits: int
        haleyCurrencyType: str
        integerAnswerValue: int

