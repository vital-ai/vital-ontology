
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class AIMPMessageContent(VITAL_Node):
        accountURI: str
        loginURI: str
        aIMPMessageContentTypeURI: str
        channelURI: str
        encodedVoiceData: str
        generatedAccumulatedText: str
        generatedText: str
        geoAPIJSON: str
        messageContentJSON: str
        text: str
        sessionID: str

