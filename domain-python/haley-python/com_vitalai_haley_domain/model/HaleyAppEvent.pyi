
import datetime
from com_vitalai_aimp_domain.model.AIMPEvent import AIMPEvent


class HaleyAppEvent(AIMPEvent):
        eventDetails: str
        eventObjectURI: str
        eventType: str

