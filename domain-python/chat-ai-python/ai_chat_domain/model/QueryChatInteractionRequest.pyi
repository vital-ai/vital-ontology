
import datetime
from ai_chat_domain.model.HaleyChatCommand import HaleyChatCommand


class QueryChatInteractionRequest(HaleyChatCommand):
        chatQueryFilter: str
        chatQueryLimit: int
        chatQueryOffset: int
        chatQuerySortDirectionURI: str
        chatQuerySortProperty: str
        chatQueryStatusURI: str
        haleyChatInteractionModelTypeURI: str
        haleyChatInteractionScopeChannelURI: str
        haleyChatInteractionScopeLoginURI: str
        haleyChatInteractionScopeURI: str
        haleyChatInteractionTypeURI: str

