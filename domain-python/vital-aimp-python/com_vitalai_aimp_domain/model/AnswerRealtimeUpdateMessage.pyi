
import datetime
from com_vitalai_aimp_domain.model.HaleyRealtimeMessage import HaleyRealtimeMessage


class AnswerRealtimeUpdateMessage(HaleyRealtimeMessage):
        propertyName: str
        propertyValue: str
        questionURI: str
        updateContent: str
        updateType: str

