
import datetime
from vital_ai_vitalsigns_core.model.VITAL_PeerEdge import VITAL_PeerEdge


class Edge_hasQuestion(VITAL_PeerEdge):
        haleyAnswerConstraintScopeType: str
        haleyAnswerValidationScopeType: str
        pageNumber: int
        questionIndex: int
        rank: int
        dynamicRequiredQuestion: bool
        highlighted: bool
        requiredQuestion: bool
        suppressedQuestion: bool

