
import datetime
from ai_chat_domain.model.HaleyChatAdminCommand import HaleyChatAdminCommand


class ResetPasswordAdminRequest(HaleyChatAdminCommand):
        accountModificationTrackingIdentifier: str
        requestedEmailAddress: str
        requestedPassword: str
        requestedRepeatedPassword: str

