
import datetime
from ai_chat_domain.model.HaleyChatUserMessage import HaleyChatUserMessage


class HaleyChatUserWritingAssistMessage(HaleyChatUserMessage):
        chatEditingInstructionsMessage: str
        chatEditingResultContentType: str
        chatEditingResultMessage: str
        chatEditingSourceContentType: str
        chatEditingSourceMessage: str

