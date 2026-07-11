
import datetime
from com_vitalai_domain_nlp.model.Document import Document


class Tweet(Document):
        authorID: int
        authorName: str
        authorScreenName: str
        favoriteCount: int
        inReplyToScreenName: str
        inReplyToTweetID: int
        inReplyToUserID: int
        originalAuthorID: int
        originalAuthorName: str
        originalAuthorScreenName: str
        retweetCount: int
        tweetID: int
        tweetStatus: str
        twitterLatitude: float
        twitterLongitude: float
        retweet: bool

