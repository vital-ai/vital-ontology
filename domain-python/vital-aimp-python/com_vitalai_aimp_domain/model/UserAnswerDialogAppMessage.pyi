
import datetime
from com_vitalai_aimp_domain.model.HaleyMessage import HaleyMessage


class UserAnswerDialogAppMessage(HaleyMessage):
        goBackSelected: bool
        helpRequested: bool
        questionClosed: bool

