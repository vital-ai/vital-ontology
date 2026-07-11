
import datetime
from ai_chat_domain.model.HaleyChatAdminCommand import HaleyChatAdminCommand


class QueryAccountOpportunityAdminRequest(HaleyChatAdminCommand):
        chatQueryFilter: str
        chatQueryLimit: int
        chatQueryOffset: int
        chatQuerySortDirectionURI: str
        chatQuerySortProperty: str
        chatQueryStatusURI: str

