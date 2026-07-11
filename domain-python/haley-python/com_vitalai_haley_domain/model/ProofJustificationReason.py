
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


class ProofJustificationReason(VITAL_Node):
    _allowed_properties = [
        {'uri': 'http://vital.ai/ontology/haley#hasProofJustificationGoal', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasProofJustificationIteration', 'prop_class': IntegerProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasProofJustificationReasonTypeURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasProofJustificationRuleIdentifier', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasProofReasonResult', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasReasonComparatorTypeURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasReasonConstraintClassURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasReasonConstraintFunctionName', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasReasonConstraintInputValue', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasReasonConstraintInstanceURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasReasonConstraintKeyName', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasReasonConstraintMLModelName', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasReasonConstraintPropertyURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasReasonConstraintValue', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasReasonConstraintValueClassURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasReasonConstraintValueDescription', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasReasonEncoding', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasReasonParse', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasReasonProvenanceURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasReasonReferenceInstanceURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasReasonReferenceTimestamp', 'prop_class': DateTimeProperty}, 
    ]

    @classmethod
    def get_allowed_properties(cls):
        return super().get_allowed_properties() + ProofJustificationReason._allowed_properties

    @classmethod
    def get_class_uri(cls) -> str:
        return 'http://vital.ai/ontology/haley#ProofJustificationReason'

