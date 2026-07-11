
import datetime
from com_vitalai_aimp_domain.model.AIMPMessage import AIMPMessage


class HaleyMessage(AIMPMessage):
        recipient: str
        slackRecipientChannelID: str
        slackRecipientTeamID: str
        slackRecipientThreadID: str
        slackRecipientUserID: str
        directMessageResponse: bool
        slackResponse: bool
        smsResponse: bool
        tweetResponse: bool
        inReplyToScreenName: str
        inReplyToTweetID: int

