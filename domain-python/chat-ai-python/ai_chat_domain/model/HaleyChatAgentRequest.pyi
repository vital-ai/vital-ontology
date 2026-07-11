
import datetime
from com_vitalai_haley_domain.model.HaleyInterAccountRequest import HaleyInterAccountRequest


class HaleyChatAgentRequest(HaleyInterAccountRequest):
        messageRequestURI: str
        accountURI: str
        loginURI: str
        channelURI: str
        requestURI: str
        sessionID: str

