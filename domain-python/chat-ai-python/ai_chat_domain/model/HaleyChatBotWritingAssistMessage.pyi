
import datetime
from ai_chat_domain.model.HaleyChatBotMessage import HaleyChatBotMessage


class HaleyChatBotWritingAssistMessage(HaleyChatBotMessage):
        chatEditingInstructionsMessage: str
        chatEditingResultContentType: str
        chatEditingResultMessage: str
        chatEditingSourceContentType: str
        chatEditingSourceMessage: str

