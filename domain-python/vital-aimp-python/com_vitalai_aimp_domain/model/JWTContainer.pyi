
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class JWTContainer(VITAL_Node):
        jweEncryptedString: str
        jweKeyIdentifier: str
        jweProviderIdentifier: str
        jwtEncodedString: str
        jwtJSON: str
        jwtKeyIdentifier: str
        jwtProviderIdentifier: str
        jwtVerified: bool

