
import datetime
from com_vitalai_aimp_domain.model.AIMPMessage import AIMPMessage


class MetaQLResultsMessage(AIMPMessage):
        bindingNames: str
        limit: int
        offset: int
        status: str
        statusMessage: str
        totalResults: int

