
import datetime
from com_vitalai_aimp_domain.model.AIMPThing import AIMPThing


class ProjectTask(AIMPThing):
        dueDate: datetime
        pecrentComplete: int
        priority: int
        projectTag: str
        shortDescription: str

