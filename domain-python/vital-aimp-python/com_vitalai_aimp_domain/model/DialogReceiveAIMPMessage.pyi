
import datetime
from com_vitalai_aimp_domain.model.DialogAction import DialogAction


class DialogReceiveAIMPMessage(DialogAction):
        expression: str
        inputPropertyName: str
        interruptedFactName: str
        propertyName: str
        timeoutPropertyName: str
        timeoutSeconds: int
        consumeImmediately: bool
        graphObjectsLinked: bool
        ignoreStandardIntents: bool
        timeoutEnabled: bool

