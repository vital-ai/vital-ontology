
import datetime
from com_vitalai_aimp_domain.model.AIMPMessage import AIMPMessage


class QuestionUpdateMessage(AIMPMessage):
        dialogPageURI: str
        index: float
        propertyName: str
        questionURI: str
        updateType: str

