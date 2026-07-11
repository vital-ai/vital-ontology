
import datetime
from ai_haley_kg_domain.model.KGNode import KGNode


class KGDocument(KGNode):
        kGContentType: str
        kGDocumentContent: str
        kGDocumentDescription: str
        kGDocumentEndTokenIndex: int
        kGDocumentExtractedContent: str
        kGDocumentHTMLContent: str
        kGDocumentHeadline: str
        kGDocumentPublicationDateTime: datetime
        kGDocumentRetrievalDateTime: datetime
        kGDocumentSegmentIndex: int
        kGDocumentSegmentMethodURI: str
        kGDocumentSegmentTokenLength: int
        kGDocumentSegmentTypeURI: str
        kGDocumentStartTokenIndex: int
        kGDocumentSummary: str
        kGDocumentTokenLength: int
        kGDocumentType: str
        kGDocumentURL: str
        kGEncodedByteData: str
        primaryLanguageType: str
        topCategoryURIs: str

