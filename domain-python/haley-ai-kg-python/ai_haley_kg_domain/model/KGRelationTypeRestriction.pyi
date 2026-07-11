
import datetime
from ai_haley_kg_domain.model.KGTypeRestriction import KGTypeRestriction


class KGRelationTypeRestriction(KGTypeRestriction):
        destinationRelationTypeRestrictionURI: str
        kGRelationTypeURI: str
        sourceRelationTypeRestrictionURI: str
        kGRelationTypeDestinationOpen: bool
        kGRelationTypeExpandDestination: bool
        kGRelationTypeExpandSource: bool
        kGRelationTypeSourceOpen: bool

