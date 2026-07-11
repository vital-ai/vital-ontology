
import datetime
from com_vitalai_aimp_domain.model.Answer import Answer


class FileAnswer(Answer):
        fileLength: int
        fileName: str
        fileType: str
        fileNodeClassURI: str
        fileNodeURI: str
        parentObjectURI: str
        url: str
        deleteOnSuccess: bool

