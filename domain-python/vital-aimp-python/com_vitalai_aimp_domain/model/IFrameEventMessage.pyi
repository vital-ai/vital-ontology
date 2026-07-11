
import datetime
from com_vitalai_aimp_domain.model.AIMPMessage import AIMPMessage


class IFrameEventMessage(AIMPMessage):
        eventType: str
        propertyValue: str

