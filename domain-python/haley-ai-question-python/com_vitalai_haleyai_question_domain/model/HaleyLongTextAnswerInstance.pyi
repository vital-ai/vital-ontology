
import datetime
from com_vitalai_haleyai_question_domain.model.HaleyAnswerInstance import HaleyAnswerInstance


class HaleyLongTextAnswerInstance(HaleyAnswerInstance):
        haleyLanguageType: str
        longTextAnalyzedAnswerValue: str
        longTextAnswerValue: str

