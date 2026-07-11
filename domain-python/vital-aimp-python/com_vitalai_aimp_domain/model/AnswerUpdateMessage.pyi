
import datetime
from com_vitalai_aimp_domain.model.AIMPMessage import AIMPMessage


class AnswerUpdateMessage(AIMPMessage):
        propertyName: str
        propertyValue: str
        questionDataJSON: str
        questionURI: str
        updateContent: str
        updateType: str

