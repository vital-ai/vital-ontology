
import datetime
from ai_haley_kg_domain.model.KGNode import KGNode


class KGFlag(KGNode):
        kGFlagDateTime: datetime
        kGFlagDescription: str
        kGFlagReasonURI: str
        kGFlagSourceURI: str
        kGFlagType: str

