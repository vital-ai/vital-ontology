
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyTaxonomyModelVersion(VITAL_Node):
        haleyTaxonomyBase: str
        haleyTaxonomyBaseVersion: str
        haleyTaxonomyModelURI: str
        haleyTaxonomyModelVersionActivateDate: datetime
        haleyTaxonomyModelVersionDeactivateDate: datetime
        activeTaxonomyModelVersion: bool

