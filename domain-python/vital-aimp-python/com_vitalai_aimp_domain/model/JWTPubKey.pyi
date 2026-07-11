
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class JWTPubKey(VITAL_Node):
        jwtKeyIdentifier: str
        jwtProviderIdentifier: str
        jwtPubKeyString: str

