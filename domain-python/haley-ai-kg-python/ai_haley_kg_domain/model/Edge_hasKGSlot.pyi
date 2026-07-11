
import datetime
from ai_haley_kg_domain.model.Edge_hasKGEdge import Edge_hasKGEdge


class Edge_hasKGSlot(Edge_hasKGEdge):
        frameGraphURI: str
        kGSlotRoleSequence: int
        kGSlotRoleType: str
        kGSlotTypeExternIdentifier: str

