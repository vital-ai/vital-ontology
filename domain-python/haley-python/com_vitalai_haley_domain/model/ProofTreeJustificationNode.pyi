
import datetime
from com_vitalai_haley_domain.model.ProofTreeNode import ProofTreeNode


class ProofTreeJustificationNode(ProofTreeNode):
        proofJustificationAnswerTypeURI: str
        proofJustificationGoal: str
        proofJustificationIteration: int
        proofJustificationResult: bool
        proofJustificationRuleIdentifier: str
        proofJustificationRuleMessage: str
        proofJustificationTypeURI: str
        finalJustification: bool

