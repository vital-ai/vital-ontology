
import datetime
from com_vitalai_domain_nlp.model.Document import Document


class YouTubeComment(Document):
        authorName: str
        channelID: str
        commentID: str
        socialLikeCount: int
        videoID: str

