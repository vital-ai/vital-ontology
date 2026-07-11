
import datetime
from com_vitalai_aimp_domain.model.DialogAction import DialogAction


class DialogPersistFact(DialogAction):
        factScope: str
        inputFactScope: str
        inputPropertyName: str
        persistFactOperationType: str
        profileURI: str
        propertyName: str
        currentProfile: bool

