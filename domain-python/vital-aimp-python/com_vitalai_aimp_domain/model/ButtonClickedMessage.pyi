
import datetime
from com_vitalai_aimp_domain.model.AIMPMessage import AIMPMessage


class ButtonClickedMessage(AIMPMessage):
        buttonURI: str
        button: str

