
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyTaxonomyModel(VITAL_Node):
        currentHaleyTaxonomyModelVersion: str
        currentHaleyTaxonomyModelVersionURI: str
        haleyTaxonomyBase: str
        haleyTaxonomyBaseVersion: str
        haleyTaxonomyModelActivateDate: datetime
        haleyTaxonomyModelDeactivateDate: datetime
        activeTaxonomyModel: bool

