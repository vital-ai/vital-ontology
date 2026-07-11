
import datetime
from com_vitalai_haley_domain.model.ProofTreeNode import ProofTreeNode


class ProofTreeDependencyNode(ProofTreeNode):
        proofJustificationGoal: str
        proofJustificationIteration: int
        proofTreeDependencyNodeOriginURIs: str

