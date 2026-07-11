
import datetime
from ai_chat_domain.model.HaleyChatMessage import HaleyChatMessage


class HaleyChatCardMessage(HaleyChatMessage):
        haleyChatIntentURI: str
        messageSerialized: str

