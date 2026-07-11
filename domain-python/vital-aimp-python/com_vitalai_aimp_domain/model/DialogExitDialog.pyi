
import datetime
from com_vitalai_aimp_domain.model.DialogAction import DialogAction


class DialogExitDialog(DialogAction):
        expression: str
        factScope: str
        nextExecutionDateMinutesSource: str
        propertyName: str
        status: str
        statusMessage: str
        keepChannelEntryText: bool

