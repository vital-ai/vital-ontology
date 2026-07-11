
import datetime
from com_vitalai_aimp_domain.model.DialogAction import DialogAction


class DialogRemoveFact(DialogAction):
        factScope: str
        propertyName: str
        removeWholeProfile: bool

