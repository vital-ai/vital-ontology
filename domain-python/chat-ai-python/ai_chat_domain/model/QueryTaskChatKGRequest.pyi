
import datetime
from ai_chat_domain.model.HaleyChatCommand import HaleyChatCommand


class QueryTaskChatKGRequest(HaleyChatCommand):
        chatQueryFilter: str
        chatQueryLimit: int
        chatQueryOffset: int
        chatQuerySortDirectionURI: str
        chatQuerySortProperty: str
        chatQueryStatusURI: str

