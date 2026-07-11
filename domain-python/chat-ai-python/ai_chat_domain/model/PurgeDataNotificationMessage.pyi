
import datetime
from ai_chat_domain.model.HaleyChatNotificationMessage import HaleyChatNotificationMessage


class PurgeDataNotificationMessage(HaleyChatNotificationMessage):
        haleyChatCacheCollectionURI: str
        haleyChatCollectionTypeURI: str
        haleyChatCommandObjectURI: str

