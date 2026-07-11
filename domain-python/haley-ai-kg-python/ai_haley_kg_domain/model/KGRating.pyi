
import datetime
from ai_haley_kg_domain.model.KGNode import KGNode


class KGRating(KGNode):
        kGRatingDateTime: datetime
        kGRatingDescription: str
        kGRatingSourceURI: str
        kGRatingStarValue: int
        kGRatingType: str
        kGRatingValueDouble: float
        kGRatingValueTypeURI: str
        kGRatingValueURI: str

