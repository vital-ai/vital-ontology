
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class ImageReference(VITAL_Node):
        contentType: str
        documentPublicationDate: datetime
        documentTitle: str
        heightPx: int
        imageURL: str
        widthPx: int

