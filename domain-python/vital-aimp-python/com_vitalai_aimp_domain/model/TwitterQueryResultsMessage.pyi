
import datetime
from com_vitalai_aimp_domain.model.TwitterMessage import TwitterMessage


class TwitterQueryResultsMessage(TwitterMessage):
        integerValue: int
        latitude: float
        longitude: float
        maxTimestamp: int
        minTimestamp: int
        radius: str
        requestType: str
        status: str
        tweetIDs: int
        countOnly: bool

