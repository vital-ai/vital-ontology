
import datetime
from com_vitalai_aimp_domain.model.DialogAction import DialogAction


class DialogTextMessage(DialogAction):
        targetChannel: str
        text: str
        textToSpeak: str
        broadcastOnly: bool
        currentChannelTarget: bool
        internalOnly: bool
        otherChannelTarget: bool
        sendAsUser: bool

