
import datetime
from com_vitalai_aimp_domain.model.UserTextMessage import UserTextMessage


class TweetTextMessage(UserTextMessage):
        sender: str
        tweetID: int

