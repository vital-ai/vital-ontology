
import datetime
from com_vitalai_aimp_domain.model.UserTextMessage import UserTextMessage


class DirectTextMessage(UserTextMessage):
        sender: str
        directMessageID: int

