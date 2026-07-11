
import datetime
from ai_chat_domain.model.HaleyChatManagerCommand import HaleyChatManagerCommand


class QueryOrgUnitManagerRequest(HaleyChatManagerCommand):
        chatQueryFilter: str
        chatQueryLimit: int
        chatQueryOffset: int
        chatQuerySortDirectionURI: str
        chatQuerySortProperty: str
        chatQueryStatusURI: str

