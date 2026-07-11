
import datetime
from com_vitalai_aimp_domain.model.AIMPMessage import AIMPMessage


class MenuClickedMessage(AIMPMessage):
        menuURI: str
        menu: str

