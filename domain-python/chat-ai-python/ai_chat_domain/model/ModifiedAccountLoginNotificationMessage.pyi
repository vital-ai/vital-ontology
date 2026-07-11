
import datetime
from ai_chat_domain.model.HaleyChatNotificationMessage import HaleyChatNotificationMessage


class ModifiedAccountLoginNotificationMessage(HaleyChatNotificationMessage):
        accountURI: str
        loginURI: str

