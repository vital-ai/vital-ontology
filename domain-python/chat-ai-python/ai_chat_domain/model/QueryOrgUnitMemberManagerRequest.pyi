
import datetime
from ai_chat_domain.model.HaleyChatManagerCommand import HaleyChatManagerCommand


class QueryOrgUnitMemberManagerRequest(HaleyChatManagerCommand):
        chatQueryFilter: str
        chatQueryLimit: int
        chatQueryOffset: int
        chatQuerySortDirectionURI: str
        chatQuerySortProperty: str
        chatQueryStatusURI: str

