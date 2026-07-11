
import datetime
from com_vitalai_aimp_domain.model.AIMPMessage import AIMPMessage


class InterAccountMessage(AIMPMessage):
        attachmentsCount: int
        subject: str

