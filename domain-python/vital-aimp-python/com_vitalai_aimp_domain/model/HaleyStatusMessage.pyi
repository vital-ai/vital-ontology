
import datetime
from com_vitalai_aimp_domain.model.HaleyMessage import HaleyMessage


class HaleyStatusMessage(HaleyMessage):
        haleyStatusMessage: str
        haleyStatusTypeURI: str
        status: str

