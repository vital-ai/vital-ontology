
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyRequest(VITAL_Node):
        requestChannelHistory: str
        requestMessageResponseSerialized: str
        requestMessageSerialized: str
        requestOriginMessageResponseSerialized: str
        requestOriginMessageSerialized: str
        requestResponseTypeURI: str
        responseChannelURI: str
        accountURI: str
        channelURI: str
        requestURI: str

