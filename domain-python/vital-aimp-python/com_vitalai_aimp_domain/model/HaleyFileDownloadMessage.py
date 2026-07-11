
from vital_ai_vitalsigns.model.properties.BooleanProperty import BooleanProperty
from vital_ai_vitalsigns.model.properties.DateTimeProperty import DateTimeProperty
from vital_ai_vitalsigns.model.properties.DoubleProperty import DoubleProperty
from vital_ai_vitalsigns.model.properties.FloatProperty import FloatProperty
from vital_ai_vitalsigns.model.properties.GeoLocationProperty import GeoLocationProperty
from vital_ai_vitalsigns.model.properties.IntegerProperty import IntegerProperty
from vital_ai_vitalsigns.model.properties.LongProperty import LongProperty
from vital_ai_vitalsigns.model.properties.OtherProperty import OtherProperty
from vital_ai_vitalsigns.model.properties.StringProperty import StringProperty
from vital_ai_vitalsigns.model.properties.TruthProperty import TruthProperty
from vital_ai_vitalsigns.model.properties.URIProperty import URIProperty
from com_vitalai_aimp_domain.model.HaleyMessage import HaleyMessage


class HaleyFileDownloadMessage(HaleyMessage):
    _allowed_properties = [
        {'uri': 'http://vital.ai/ontology/vital#hasFileLength', 'prop_class': LongProperty}, 
        {'uri': 'http://vital.ai/ontology/vital#hasFileName', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital#hasFileScope', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital#hasFileType', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital#hasFileURL', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasFileNodeURI', 'prop_class': URIProperty}, 
    ]

    @classmethod
    def get_allowed_properties(cls):
        return super().get_allowed_properties() + HaleyFileDownloadMessage._allowed_properties

    @classmethod
    def get_class_uri(cls) -> str:
        return 'http://vital.ai/ontology/vital-aimp#HaleyFileDownloadMessage'

