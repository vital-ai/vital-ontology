
import datetime
from ai_haley_kg_domain.model.KGNode import KGNode


class KGAgentSubmission(KGNode):
        kGAgentSubmissionComments: str
        kGAgentSubmissionCreator: str
        kGAgentSubmissionDateTime: datetime
        kGAgentSubmissionDescription: str
        kGAgentSubmissionName: str
        kGAgentSubmissionSubmitterEmail: str
        kGAgentSubmissionSubmitterName: str
        kGAgentSubmissionType: str
        kGAgentSubmissionURL: str
        kGAgentSubmissionApproved: bool
        kGAgentSubmissionConverted: bool
        kGAgentSubmissionReviewed: bool

