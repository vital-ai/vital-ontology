
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyMindMetaQLDataset(VITAL_Node):
        ruleInvocationURI: str
        ruleMetaQLObjectCount: int
        ruleMetaQLParameterMap: str
        ruleMetaQLQueryName: str
        ruleMetaQLTimestamp: datetime
        ruleProvenanceURI: str
        ruleURI: str

