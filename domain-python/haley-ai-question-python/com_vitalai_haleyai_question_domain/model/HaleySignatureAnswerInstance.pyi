
import datetime
from com_vitalai_haleyai_question_domain.model.HaleyAnswerInstance import HaleyAnswerInstance


class HaleySignatureAnswerInstance(HaleyAnswerInstance):
        answerInstanceImageHeight: str
        answerInstanceImageURL: str
        answerInstanceImageWidth: str
        haleySignatureAnswerStyleURI: str
        signatureAnswerValue: str
        anchorAnswerInstance: bool

