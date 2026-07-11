
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
from com_vitalai_haley_domain.model.ProofTreeNode import ProofTreeNode


class ProofTreeJustificationNode(ProofTreeNode):
    _allowed_properties = [
        {'uri': 'http://vital.ai/ontology/haley#hasProofJustificationAnswerTypeURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasProofJustificationGoal', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasProofJustificationIteration', 'prop_class': IntegerProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasProofJustificationResult', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasProofJustificationRuleIdentifier', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasProofJustificationRuleMessage', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasProofJustificationTypeURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#isFinalJustification', 'prop_class': BooleanProperty}, 
    ]

    @classmethod
    def get_allowed_properties(cls):
        return super().get_allowed_properties() + ProofTreeJustificationNode._allowed_properties

    @classmethod
    def get_class_uri(cls) -> str:
        return 'http://vital.ai/ontology/haley#ProofTreeJustificationNode'

