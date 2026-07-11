
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
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyValidationPathInstance(VITAL_Node):
    _allowed_properties = [
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasAvailablePathInstanceChoiceValues', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasAvailablePathInstanceLowerDateTimeValue', 'prop_class': DateTimeProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasAvailablePathInstanceLowerDoubleValue', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasAvailablePathInstanceLowerIntegerValue', 'prop_class': IntegerProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasAvailablePathInstanceMultiChoiceValues', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasAvailablePathInstanceTaxonomyURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasAvailablePathInstanceUpperDateTimeValue', 'prop_class': DateTimeProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasAvailablePathInstanceUpperDoubleValue', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasAvailablePathInstanceUpperIntegerValue', 'prop_class': IntegerProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasHaleyAnswerInstance', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasHaleyAnswerInstances', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasHaleyAnswerType', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasHaleyClassURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasHaleyGroup', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasHaleyGroupInstance', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasHaleyObjectURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasHaleyPropertyURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasHaleyRootClassURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasHaleyRowInstanceCounter', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasHaleyRowRowInstanceCounter', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasHaleyRowRowTypeURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasHaleyRowTypeURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasPathInstanceBooleanValue', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasPathInstanceChoiceValue', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasPathInstanceDateTimeValue', 'prop_class': DateTimeProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasPathInstanceDoubleValue', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasPathInstanceIntegerValue', 'prop_class': IntegerProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasPathInstanceLongTextValue', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasPathInstanceMultiChoiceValue', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasPathInstanceRootURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasPathInstanceTaxonomyValue', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasPathInstanceTextValue', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasPathInstanceUnknownValue', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasPathInstanceUriValue', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasProofTreeMembershipURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasSourceProvenanceURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasValidationPathConstraintType', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasValidationPathInstanceMessage', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasValidationPathScopeType', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasValidationPathType', 'prop_class': URIProperty}, 
    ]

    @classmethod
    def get_allowed_properties(cls):
        return super().get_allowed_properties() + HaleyValidationPathInstance._allowed_properties

    @classmethod
    def get_class_uri(cls) -> str:
        return 'http://vital.ai/ontology/haley-ai-question#HaleyValidationPathInstance'

