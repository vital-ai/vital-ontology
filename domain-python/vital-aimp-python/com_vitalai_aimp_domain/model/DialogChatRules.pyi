
import datetime
from com_vitalai_aimp_domain.model.DialogAction import DialogAction


class DialogChatRules(DialogAction):
        chatRuleProcessingType: str
        inputFactScope: str
        inputPropertyName: str
        intentPropertyName: str
        interruptedFactName: str
        outputCardsPropertyName: str
        outputMessagePropertyName: str
        propertyName: str
        propertyType: str
        statusPropertyName: str
        ignoreStandardIntents: bool

