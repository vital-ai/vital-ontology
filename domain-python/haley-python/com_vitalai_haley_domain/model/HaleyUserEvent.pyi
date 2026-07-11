
import datetime
from com_vitalai_haley_domain.model.HaleyAppEvent import HaleyAppEvent


class HaleyUserEvent(HaleyAppEvent):
        loginUsername: str
        loginURI: str

