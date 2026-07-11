
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyAnswerPathCriterion(VITAL_Node):
        haleyAnswerConstraintComparatorURI: str
        haleyAnswerType: str
        haleyClassURI: str
        haleyGroup: str
        haleyGroupInstance: str
        haleyObjectURI: str
        haleyPropertyURI: str
        haleyRootClassURI: str
        haleyRowInstanceCounter: str
        haleyRowRowInstanceCounter: str
        haleyRowRowTypeURI: str
        haleyRowTypeURI: str
        pathInstanceBooleanValue: bool
        pathInstanceChoiceValue: str
        pathInstanceDateTimeValue: datetime
        pathInstanceDoubleValue: float
        pathInstanceIntegerValue: int
        pathInstanceLongTextValue: str
        pathInstanceMultiChoiceValue: str
        pathInstanceMultiTaxonomyValue: str
        pathInstanceRootURI: str
        pathInstanceTaxonomyValue: str
        pathInstanceTextValue: str
        pathInstanceUnknownValue: str
        pathInstanceUriValue: str
        sourceProvenanceURI: str
        haleyQuerySubclassExpansion: bool

