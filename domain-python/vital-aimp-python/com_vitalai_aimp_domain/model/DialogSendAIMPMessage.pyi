
import datetime
from com_vitalai_aimp_domain.model.DialogAction import DialogAction


class DialogSendAIMPMessage(DialogAction):
        factScope: str
        messageSerialized: str
        propertyName: str
        requestType: str
        targetChannel: str
        broadcastOnly: bool
        currentChannelTarget: bool
        internalOnly: bool
        otherChannelTarget: bool
        sendAsUser: bool

