
import datetime
from com_vitalai_aimp_domain.model.UserTextMessage import UserTextMessage


class SlackTextMessage(UserTextMessage):
        slackChannelID: str
        slackEventType: str
        slackFileShareName: str
        slackFileShareURL: str
        slackMessageJSON: str
        slackTeamID: str
        slackThreadID: str
        slackUserID: str

