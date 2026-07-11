
import datetime
from com_vitalai_aimp_domain.model.DialogElement import DialogElement


class DialogQuestion(DialogElement):
        factClassName: str
        factPropertyName: str
        parentFactURI: str
        validationType: str
        sent: bool

