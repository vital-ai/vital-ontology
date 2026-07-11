
import datetime
from com_vitalai_aimp_domain.model.Card import Card


class Device(Card):
        channels: str
        color: str
        deviceType: str
        imageURL: str
        lastActiveDate: datetime

