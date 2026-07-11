
import datetime
from com_vitalai_aimp_domain.model.HaleyMessage import HaleyMessage


class HaleyFileDownloadMessage(HaleyMessage):
        fileLength: int
        fileName: str
        fileScope: str
        fileType: str
        fileURL: str
        fileNodeURI: str

