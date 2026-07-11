
import datetime
from com_vitalai_aimp_domain.model.TwitterMessage import TwitterMessage


class TwitterQueryRequestMessage(TwitterMessage):
        latitude: float
        longitude: float
        maxTimestamp: int
        minTimestamp: int
        radius: str
        requestType: str
        tweetIDs: int
        countOnly: bool
        queryString: str

