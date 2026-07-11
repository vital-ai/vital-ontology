
import datetime
from com_vitalai_aimp_domain.model.ListFact import ListFact


class ResultListFact(ListFact):
        bindingNames: str
        limit: int
        offset: int
        status: str
        statusMessage: str
        totalResults: int

