
import datetime
from com_vitalai_aimp_domain.model.AIMPMessage import AIMPMessage


class RemoveQuestionMessage(AIMPMessage):
        dialogPageURI: str
        questionURI: str

