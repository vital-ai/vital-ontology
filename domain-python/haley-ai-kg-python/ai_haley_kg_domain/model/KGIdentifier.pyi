
import datetime
from ai_haley_kg_domain.model.KGNode import KGNode


class KGIdentifier(KGNode):
        kGIdentifierEnclosingID: str
        kGIdentifierEnclosingURI: str
        kGIdentifierPrimaryID: str
        kGIdentifierPrimaryURI: str
        kGIdentifierSecondaryID: str
        kGIdentifierSecondaryURI: str
        kGIdentifierSourceURI: str

