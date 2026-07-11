
import datetime
from com_vitalai_aimp_domain.model.CommandMessage import CommandMessage


class GetObjectMessage(CommandMessage):
        objectURI: str
        includeDependentObjects: bool

