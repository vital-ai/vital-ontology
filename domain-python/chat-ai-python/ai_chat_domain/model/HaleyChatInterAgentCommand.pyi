
import datetime
from com_vitalai_haley_domain.model.HaleyRequestMessage import HaleyRequestMessage


class HaleyChatInterAgentCommand(HaleyRequestMessage):
        callingInteractionURI: str
        haleyChatInterAgentCommandTypeURI: str
        respondingInteractionURI: str

