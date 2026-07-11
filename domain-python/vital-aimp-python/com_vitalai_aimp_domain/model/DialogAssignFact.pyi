
import datetime
from com_vitalai_aimp_domain.model.DialogAction import DialogAction


class DialogAssignFact(DialogAction):
        expression: str
        factScope: str
        inputFactScope: str
        inputPropertyName: str
        propertyName: str
        propertyType: str
        propertyValue: str
        graphObjectsLinked: bool

