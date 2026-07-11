
import datetime
from com_vitalai_aimp_domain.model.DialogAction import DialogAction


class DialogDownloadFile(DialogAction):
        fileScope: str
        factScope: str
        propertyName: str
        targetChannel: str
        text: str
        broadcastOnly: bool
        currentChannelTarget: bool
        internalOnly: bool
        otherChannelTarget: bool
        sendAsUser: bool

