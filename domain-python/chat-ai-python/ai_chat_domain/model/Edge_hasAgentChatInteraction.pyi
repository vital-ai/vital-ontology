
import datetime
from vital_ai_vitalsigns_core.model.VITAL_PeerEdge import VITAL_PeerEdge


class Edge_hasAgentChatInteraction(VITAL_PeerEdge):
        agentChatInteractionStatusMessage: str
        agentChatInteractionStatusURI: str
        agentChatInteractionTypeURI: str
        callingAgentInstallURI: str
        respondingAgentInstallURI: str

