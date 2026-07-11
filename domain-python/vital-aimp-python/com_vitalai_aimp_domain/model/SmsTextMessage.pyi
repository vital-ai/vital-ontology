
import datetime
from com_vitalai_aimp_domain.model.UserTextMessage import UserTextMessage


class SmsTextMessage(UserTextMessage):
        recipient: str
        sender: str
        mms: bool

