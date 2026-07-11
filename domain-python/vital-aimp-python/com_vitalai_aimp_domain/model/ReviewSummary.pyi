
import datetime
from com_vitalai_domain_nlp.model.Document import Document


class ReviewSummary(Document):
        averageRating: float
        parentURI: str
        totalReviews: int

