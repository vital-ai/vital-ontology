
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class KGCriterion(VITAL_Node):
        kGConstraintComparatorURI: str
        kGCriterionTypeURI: str
        kGQueryBooleanValue: bool
        kGQueryChoiceValue: str
        kGQueryClassURI: str
        kGQueryDateTimeValue: datetime
        kGQueryDoubleValue: float
        kGQueryIntegerValue: int
        kGQueryKGMetaType: str
        kGQueryKGNodeClassURI: str
        kGQueryKGRelationType: str
        kGQueryKGType: str
        kGQueryLongTextValue: str
        kGQueryMoveFromConcepts: str
        kGQueryMoveToConcepts: str
        kGQueryMultiChoiceValue: str
        kGQueryMultiTaxonomyValue: str
        kGQueryNearVectorCertainty: float
        kGQueryNearVectorDistance: float
        kGQueryNearVectorForce: float
        kGQueryObjectURI: str
        kGQueryPropertyURI: str
        kGQueryProvenanceURI: str
        kGQueryRootURI: str
        kGQuerySerializedVector: str
        kGQueryTaxonomyValue: str
        kGQueryTextValue: str
        kGQueryTopKLimit: int
        kGQueryURIValue: str
        kGQueryUnknownValue: str
        kGQuerySubclassExpansion: bool
        kGQuerySubtypeExpansion: bool

