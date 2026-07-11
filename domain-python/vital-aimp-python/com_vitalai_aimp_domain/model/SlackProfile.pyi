
import datetime
from com_vitalai_aimp_domain.model.EndpointProfile import EndpointProfile


class SlackProfile(EndpointProfile):
        slackTeamID: str
        slackThreadID: str
        slackUserID: str

