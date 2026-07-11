
import datetime
from com_vitalai_aimp_domain.model.CommandMessage import CommandMessage


class SearchRequestMessage(CommandMessage):
        limit: int
        offset: int
        searchCategoryURI: str
        searchExcludedCategoryURI: str
        searchGeoURI: str
        userCategoryURI: str
        queryString: str

