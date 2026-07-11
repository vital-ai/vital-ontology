
import datetime
from ai_haley_kg_domain.model.KGNode import KGNode


class KGCodeDocument(KGNode):
        kGCodeDocumentType: str
        kGCodeInterpreterVersion: str
        kGCodeLanguageURI: str
        kGCodeLanguageVersion: str
        kGSourceCode: str

