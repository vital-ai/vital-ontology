
import datetime
from ai_haley_kg_domain.model.KGNode import KGNode


class KGAgent(KGNode):
        kGAgentAvatarImageSourceURL: str
        kGAgentAvatarImageURL: str
        kGAgentAvatarLargeImageURL: str
        kGAgentDeploymentURL: str
        kGAgentDescription: str
        kGAgentIdentifier: str
        kGAgentImplIdentifier: str
        kGAgentModificationDateTime: datetime
        kGAgentName: str
        kGAgentNameSlug: str
        kGAgentPublishStatusURI: str
        kGAgentPublisherName: str
        kGAgentRankingScore: float
        kGAgentRankingScoreUpdateDateTime: datetime
        kGAgentServiceURIs: str
        kGAgentType: str
        kGBracketURIs: str
        primaryLanguageType: str
        topCategoryURIs: str

