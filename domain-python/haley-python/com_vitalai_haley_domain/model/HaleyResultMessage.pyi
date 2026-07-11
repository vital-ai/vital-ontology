
import datetime
from com_vitalai_haley_domain.model.HaleyResponseMessage import HaleyResponseMessage


class HaleyResultMessage(HaleyResponseMessage):
        haleyLimit: int
        haleyOffset: int
        haleyTotalResults: int
        resultSequence: int

