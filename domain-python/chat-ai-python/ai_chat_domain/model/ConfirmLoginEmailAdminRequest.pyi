
import datetime
from ai_chat_domain.model.HaleyChatAdminCommand import HaleyChatAdminCommand


class ConfirmLoginEmailAdminRequest(HaleyChatAdminCommand):
        accountModificationTrackingIdentifier: str

