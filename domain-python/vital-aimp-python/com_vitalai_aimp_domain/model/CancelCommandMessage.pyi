
import datetime
from com_vitalai_aimp_domain.model.UserInterfaceCommandMessage import UserInterfaceCommandMessage


class CancelCommandMessage(UserInterfaceCommandMessage):
        cancelCommandMessageURI: str
        cancelCommandObjectURI: str

