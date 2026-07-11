
import datetime
from com_vitalai_aimp_domain.model.AIMPCommandMessage import AIMPCommandMessage


class AIMPCommand(AIMPCommandMessage):
        aIMPCommandOperationType: str
        aIMPCommandTargetClassURI: str
        aIMPCommandTargetObjectURI: str
        aIMPCommandTargetRootURI: str
        aIMPCommandType: str

