
import datetime
from com_vitalai_aimp_domain.model.AIMPMessage import AIMPMessage


class VirtualLoginResponseMessage(AIMPMessage):
        status: str
        statusMessage: str

