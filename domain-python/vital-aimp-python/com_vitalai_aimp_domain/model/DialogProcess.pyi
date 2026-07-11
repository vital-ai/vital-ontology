
import datetime
from com_vitalai_aimp_domain.model.DialogAction import DialogAction


class DialogProcess(DialogAction):
        errorMessagePropertyName: str
        factScope: str
        inputFactScope: str
        inputPropertyName: str
        processorType: str
        propertyName: str
        statusPropertyName: str
        timeoutSeconds: int
        graphObjectsLinked: bool

