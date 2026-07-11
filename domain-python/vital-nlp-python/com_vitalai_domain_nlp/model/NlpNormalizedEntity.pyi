
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class NlpNormalizedEntity(VITAL_Node):
        context: str
        entityType: str
        heightPx: int
        imageDate: datetime
        imageURL: str
        nameVariants: str
        nlpEntityCategory: str
        shortname: str
        symbol: str
        ticker: str
        widthPx: int
        wikipediaURL: str
        wordnetURI: str

