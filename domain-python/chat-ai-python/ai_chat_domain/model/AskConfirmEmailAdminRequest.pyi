
import datetime
from ai_chat_domain.model.HaleyChatAdminCommand import HaleyChatAdminCommand


class AskConfirmEmailAdminRequest(HaleyChatAdminCommand):
        requestedEmailAddress: str

