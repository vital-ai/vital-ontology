
import datetime
from ai_chat_domain.model.HaleyChatAdminCommand import HaleyChatAdminCommand


class AskResetPasswordAdminRequest(HaleyChatAdminCommand):
        requestedEmailAddress: str

