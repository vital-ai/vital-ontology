
import datetime
from ai_haley_kg_domain.model.KGNode import KGNode


class KGStatsSummary(KGNode):
        kGStatsSummaryCount: int
        kGStatsSummaryCountPercentage: float
        kGStatsSummaryPeriod: datetime
        kGStatsSummaryPeriodDay: int
        kGStatsSummaryPeriodMonth: int
        kGStatsSummaryPeriodYear: int
        kGStatsSummaryType: str

