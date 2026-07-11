
import datetime
from com_vitalai_haleyai_question_domain.model.HaleyAnswerInstance import HaleyAnswerInstance


class HaleyTextAnswerInstance(HaleyAnswerInstance):
        haleyLanguageType: str
        textAnalyzedAnswerValue: str
        textAnswerValue: str

