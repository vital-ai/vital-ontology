
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class TaxonomyNode(VITAL_Node):
        externalID: str
        leafCategory: bool
        rootCategory: bool
        selectable: bool
        description: str

