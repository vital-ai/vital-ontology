
import datetime
from ai_chat_domain.model.HaleyChatCommand import HaleyChatCommand


class GetInteractionCostRequest(HaleyChatCommand):
        agentInstallURI: str
        haleyChatInteractionModelTypeURI: str

