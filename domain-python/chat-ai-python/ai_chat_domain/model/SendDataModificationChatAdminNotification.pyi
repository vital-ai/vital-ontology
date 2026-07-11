
import datetime
from ai_chat_domain.model.HaleyChatAdminNotification import HaleyChatAdminNotification


class SendDataModificationChatAdminNotification(HaleyChatAdminNotification):
        dataModificationEventType: str
        dataModificationGraphObjectClassURI: str
        dataModificationObjectURI: str

