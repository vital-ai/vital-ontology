
import datetime
from com_vitalai_haley_domain.model.HaleyInterAccountResponse import HaleyInterAccountResponse


class HaleyChatAgentResponse(HaleyInterAccountResponse):
        messageRequestURI: str
        accountURI: str
        loginURI: str
        channelURI: str
        requestURI: str
        sessionID: str

