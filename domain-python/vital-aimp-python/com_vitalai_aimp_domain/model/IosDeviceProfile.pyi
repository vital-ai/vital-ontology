
import datetime
from com_vitalai_aimp_domain.model.EndpointProfile import EndpointProfile


class IosDeviceProfile(EndpointProfile):
        token: str
        uuid: str
        notificationsEnabled: bool

