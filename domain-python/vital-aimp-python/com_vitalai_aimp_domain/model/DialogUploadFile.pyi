
import datetime
from com_vitalai_aimp_domain.model.DialogAction import DialogAction


class DialogUploadFile(DialogAction):
        fileScope: str
        factPropertyName: str
        factScope: str
        fileUploadProcessingType: str
        inputFactScope: str
        inputFileFactName: str
        inputFileFactScope: str
        inputPropertyName: str
        interruptedFactName: str
        propertyName: str
        targetChannel: str
        text: str
        broadcastOnly: bool
        currentChannelTarget: bool
        ignoreStandardIntents: bool
        internalOnly: bool
        otherChannelTarget: bool
        sendAsUser: bool
        skippable: bool

