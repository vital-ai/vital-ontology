
import datetime
from com_vitalai_aimp_domain.model.HaleyMessage import HaleyMessage


class HaleyActivityMessage(HaleyMessage):
        activityCanceled: bool
        activityComplete: bool

