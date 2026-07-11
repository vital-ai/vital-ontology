
import datetime
from com_vitalai_aimp_domain.model.DialogAction import DialogAction


class DialogRecommend(DialogAction):
        errorMessagePropertyName: str
        propertyName: str
        statusPropertyName: str
        timeoutSeconds: int
        graphObjectsLinked: bool

