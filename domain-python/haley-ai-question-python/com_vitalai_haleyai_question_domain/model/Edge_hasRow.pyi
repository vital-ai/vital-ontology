
import datetime
from vital_ai_vitalsigns_core.model.VITAL_PeerEdge import VITAL_PeerEdge


class Edge_hasRow(VITAL_PeerEdge):
        maximumRowCount: int
        minimumRowCount: int
        questionIndex: int
        highlighted: bool
        requiredRow: bool
        suppressedRow: bool

