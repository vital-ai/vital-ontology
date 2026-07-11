
import datetime
from com_vitalai_aimp_domain.model.DialogAction import DialogAction


class DialogDatascriptAction(DialogAction):
        errorMessagePropertyName: str
        propertyName: str
        scriptBody: str
        statusPropertyName: str
        timeoutSeconds: int
        graphObjectsLinked: bool

