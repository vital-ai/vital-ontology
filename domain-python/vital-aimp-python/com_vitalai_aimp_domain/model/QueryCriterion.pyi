
import datetime
from com_vitalai_aimp_domain.model.DialogPart import DialogPart


class QueryCriterion(DialogPart):
        comparator: str
        criterionType: str
        propertyName: str
        propertyValue: str

