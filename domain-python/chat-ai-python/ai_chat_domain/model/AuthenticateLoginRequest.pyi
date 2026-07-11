
import datetime
from ai_chat_domain.model.HaleyChatCommand import HaleyChatCommand


class AuthenticateLoginRequest(HaleyChatCommand):
        authPassword: str

