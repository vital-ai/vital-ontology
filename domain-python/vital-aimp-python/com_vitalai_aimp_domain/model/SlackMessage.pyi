
import datetime
from com_vitalai_aimp_domain.model.AIMPMessage import AIMPMessage


class SlackMessage(AIMPMessage):
        slackChannelID: str
        slackEventType: str
        slackTeamID: str
        slackThreadID: str
        slackUserID: str

