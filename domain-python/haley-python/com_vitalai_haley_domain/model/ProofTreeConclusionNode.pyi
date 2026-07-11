
import datetime
from com_vitalai_haley_domain.model.ProofTreeNode import ProofTreeNode


class ProofTreeConclusionNode(ProofTreeNode):
        proofAnswerTypeURI: str
        proofConclusionExplanation: str
        proofDecisionURI: str
        proofPrimaryGoalURI: str
        proofTertiaryGoalURI: str

