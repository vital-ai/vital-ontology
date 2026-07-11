
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class Endpoint(VITAL_Node):
        endpointID: str
        channelRandomized: bool
        defaultEndpoint: bool
        tunnelingEnabled: bool

