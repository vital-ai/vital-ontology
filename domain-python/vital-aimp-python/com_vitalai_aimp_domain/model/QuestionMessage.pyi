
import datetime
from com_vitalai_aimp_domain.model.AIMPMessage import AIMPMessage


class QuestionMessage(AIMPMessage):
        dialogPageURI: str
        index: float
        parentQuestionURI: str
        previousAnswer: str
        questionContent: str
        questionOption: str
        questionPreviousContent: str
        slackRecipientChannelID: str
        slackRecipientTeamID: str
        slackRecipientThreadID: str
        slackRecipientUserID: str
        slackResponse: bool

