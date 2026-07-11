
import datetime
from com_vitalai_aimp_domain.model.DialogPart import DialogPart


class Choice(DialogPart):
        backgroundColor: str
        choiceLabel: str
        choiceValue: str
        color: str
        imageURL: str
        index: float
        exclusive: bool

