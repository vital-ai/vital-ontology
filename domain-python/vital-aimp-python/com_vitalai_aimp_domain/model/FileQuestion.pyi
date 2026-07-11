
import datetime
from com_vitalai_aimp_domain.model.Question import Question


class FileQuestion(Question):
        fileScope: str
        fileTypeConstraint: str
        maxFileLength: int

