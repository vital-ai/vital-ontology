
import datetime
from com_vitalai_aimp_domain.model.DialogAction import DialogAction


class DialogPayment(DialogAction):
        errorMessagePropertyName: str
        id: str
        propertyName: str
        statusPropertyName: str
        timeoutSeconds: int

