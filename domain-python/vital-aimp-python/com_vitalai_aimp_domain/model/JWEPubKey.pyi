
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class JWEPubKey(VITAL_Node):
        jweKeyIdentifier: str
        jweProviderIdentifier: str
        jwePubKeyString: str

