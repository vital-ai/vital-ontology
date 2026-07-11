
import datetime
from com_vitalai_aimp_domain.model.Question import Question


class TrueFalseQuestion(Question):
        choiceListSource: str
        falseLabel: str
        inputFactScope: str
        inputPropertyName: str
        trueLabel: str
        renderQuickReplies: bool
        trueAnswerOnly: bool

