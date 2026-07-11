
import datetime
from com_vitalai_aimp_domain.model.CommandMessage import CommandMessage


class UnsetFactMessage(CommandMessage):
        booleanValue: bool
        doubleValue: float
        factClassName: str
        factScope: str
        geolocation: str
        integerValue: int
        propertyName: str
        stringValue: str
        truthValue: str
        includeSubclasses: bool

