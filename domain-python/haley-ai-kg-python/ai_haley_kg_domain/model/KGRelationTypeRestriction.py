
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
from ai_haley_kg_domain.model.KGTypeRestriction import KGTypeRestriction


class KGRelationTypeRestriction(KGTypeRestriction):
    _allowed_properties = [
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasDestinationRelationTypeRestrictionURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGRelationTypeURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasSourceRelationTypeRestrictionURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#isKGRelationTypeDestinationOpen', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#isKGRelationTypeExpandDestination', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#isKGRelationTypeExpandSource', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#isKGRelationTypeSourceOpen', 'prop_class': BooleanProperty}, 
    ]

    @classmethod
    def get_allowed_properties(cls):
        return super().get_allowed_properties() + KGRelationTypeRestriction._allowed_properties

    @classmethod
    def get_class_uri(cls) -> str:
        return 'http://vital.ai/ontology/haley-ai-kg#KGRelationTypeRestriction'

