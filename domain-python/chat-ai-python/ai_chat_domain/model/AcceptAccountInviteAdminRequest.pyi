
import datetime
from ai_chat_domain.model.HaleyChatAdminCommand import HaleyChatAdminCommand


class AcceptAccountInviteAdminRequest(HaleyChatAdminCommand):
        accountModificationTrackingIdentifier: str
        requestedAccountName: str
        requestedLoginName: str
        requestedPassword: str
        requestedRepeatedPassword: str

