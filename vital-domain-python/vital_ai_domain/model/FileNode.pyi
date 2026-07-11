
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class FileNode(VITAL_Node):
        accountURI: str
        expirationDate: datetime
        fileLength: int
        fileName: str
        fileScope: str
        fileType: str
        fileURL: str
        profileURI: str

