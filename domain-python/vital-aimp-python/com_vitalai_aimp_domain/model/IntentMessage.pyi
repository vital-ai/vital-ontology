
import datetime
from com_vitalai_aimp_domain.model.CommandMessage import CommandMessage


class IntentMessage(CommandMessage):
        intent: str
        propertyValue: str

