
import datetime
from com_vitalai_aimp_domain.model.Question import Question


class MultiChoiceQuestion(Question):
        choiceListSource: str
        inputFactScope: str
        inputPropertyName: str
        submitButtonLabel: str
        multivalue: bool
        renderQuickReplies: bool

