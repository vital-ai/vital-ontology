
import datetime
from com_vitalai_aimp_domain.model.AIMPMessage import AIMPMessage


class ButtonStateMessage(AIMPMessage):
        nextButtonLabel: str
        previousButtonLabel: str
        submitButtonLabel: str
        nextButtonEnabled: bool
        previousButtonEnabled: bool
        submitButtonEnabled: bool

