
import datetime
from com_vitalai_aimp_domain.model.AIMPMessage import AIMPMessage


class AnswerMessage(AIMPMessage):
        dialogPageURI: str
        slackChannelID: str
        slackEventType: str
        slackTeamID: str
        slackThreadID: str
        slackUserID: str
        answerSkipped: bool
        goBackSelected: bool
        helpRequested: bool
        questionClosed: bool
        slackResponse: bool

