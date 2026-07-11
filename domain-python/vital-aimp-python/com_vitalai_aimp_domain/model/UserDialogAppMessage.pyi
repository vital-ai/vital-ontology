
import datetime
from com_vitalai_aimp_domain.model.HaleyMessage import HaleyMessage


class UserDialogAppMessage(HaleyMessage):
        answerSkipped: bool
        goBackSelected: bool
        helpRequested: bool
        questionClosed: bool

