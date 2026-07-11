
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class ProofJustificationReason(VITAL_Node):
        proofJustificationGoal: str
        proofJustificationIteration: int
        proofJustificationReasonTypeURI: str
        proofJustificationRuleIdentifier: str
        proofReasonResult: bool
        reasonComparatorTypeURI: str
        reasonConstraintClassURI: str
        reasonConstraintFunctionName: str
        reasonConstraintInputValue: str
        reasonConstraintInstanceURI: str
        reasonConstraintKeyName: str
        reasonConstraintMLModelName: str
        reasonConstraintPropertyURI: str
        reasonConstraintValue: str
        reasonConstraintValueClassURI: str
        reasonConstraintValueDescription: str
        reasonEncoding: str
        reasonParse: str
        reasonProvenanceURI: str
        reasonReferenceInstanceURI: str
        reasonReferenceTimestamp: datetime

