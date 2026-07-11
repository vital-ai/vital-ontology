
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class AIMPMessageMetaInfo(VITAL_Node):
        messageChannelHistory: str
        messageChildChannelURI: str
        messageParentChannelURI: str
        messageReceiveDateTime: datetime
        messageRequestURI: str
        messageSourceChannelURI: str
        messageURI: str

