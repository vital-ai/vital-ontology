
import datetime
from com_vitalai_aimp_domain.model.AIMPMessage import AIMPMessage


class AnswerStatusMessage(AIMPMessage):
        propertyName: str
        propertyValue: str
        questionURI: str
        status: str
        statusMessage: str
        updateContent: str
        updateType: str
        updateAnswer: bool

