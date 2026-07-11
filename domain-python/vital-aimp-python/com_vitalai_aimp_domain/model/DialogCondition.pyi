
import datetime
from com_vitalai_aimp_domain.model.DialogPart import DialogPart


class DialogCondition(DialogPart):
        comparator: str
        conditionType: str
        expression: str
        factScope: str
        propertyName: str
        propertyValue: str
        subpropertyName: str
        subpropertyEnabled: bool

