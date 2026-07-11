
import datetime
from ai_chat_domain.model.HaleyChatCommand import HaleyChatCommand


class QueryAssetRequest(HaleyChatCommand):
        chatQueryFilter: str
        chatQueryLimit: int
        chatQueryOffset: int
        chatQuerySortDirectionURI: str
        chatQuerySortProperty: str
        chatQueryStatusURI: str

