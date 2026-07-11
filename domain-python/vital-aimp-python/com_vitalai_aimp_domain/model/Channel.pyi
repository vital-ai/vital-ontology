
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class Channel(VITAL_Node):
        agentInstanceDeploymentURI: str
        botURI: str
        channelTypeURI: str
        lastActivityTime: int
        orderInUI: int
        orientationInUI: str
        stateManager: str
        anonymousChannel: bool
        childChannel: bool
        defaultChannel: bool
        displayInUI: bool
        haleyMessageTextHidden: bool
        systemChannel: bool
        textEntryHidden: bool

