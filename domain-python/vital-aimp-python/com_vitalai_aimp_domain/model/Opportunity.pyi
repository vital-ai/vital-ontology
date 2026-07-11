
import datetime
from com_vitalai_aimp_domain.model.AIMPThing import AIMPThing


class Opportunity(AIMPThing):
        entityURI: str
        objectURI: str
        opportunityStatus: str
        shortDescription: str

