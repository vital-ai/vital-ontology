
import datetime
from com_vitalai_aimp_domain.model.DeviceMessage import DeviceMessage


class DeviceStateChangeMessage(DeviceMessage):
        deviceNewState: str
        deviceOldState: str

