
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class Image(VITAL_Node):
        contentType: str
        documentPublicationDate: datetime
        documentTitle: str
        heightPx: int
        imageData: str
        widthPx: int

