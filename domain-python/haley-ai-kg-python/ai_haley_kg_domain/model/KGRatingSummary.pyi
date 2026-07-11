
import datetime
from ai_haley_kg_domain.model.KGNode import KGNode


class KGRatingSummary(KGNode):
        kGRatingCalculationDateTime: datetime
        kGRatingSummaryAverageRatingDouble: float
        kGRatingSummaryAverageStarRating: float
        kGRatingSummaryNegativeCount: int
        kGRatingSummaryNeutralCount: int
        kGRatingSummaryPositiveCount: int
        kGRatingSummaryReviewCount: int
        kGRatingSummaryText: str
        kGRatingSummaryTitle: str
        kGRatingSummaryTotalCount: int
        kGRatingSummaryType: str
        kGRatingValueTypeURI: str

