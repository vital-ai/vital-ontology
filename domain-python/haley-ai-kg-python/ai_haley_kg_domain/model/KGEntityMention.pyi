
import datetime
from ai_haley_kg_domain.model.KGNode import KGNode


class KGEntityMention(KGNode):
        kGEntityAccountURI: str
        kGEntityLoginURI: str
        kGEntityType: str
        kGEntityTypeDescription: str
        kGExtractTaskURI: str
        kGTypeMethodURI: str

