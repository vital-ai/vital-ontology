
import datetime
from ai_chat_domain.model.HaleyChatCommand import HaleyChatCommand


class GetChannelOrgMembersRequest(HaleyChatCommand):
        requestedChannelURI: str

