
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


class HaleyAnswerConstraint(VITAL_Node):
    _allowed_properties = [
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasBooleanAnswerValue', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasChoiceAnswerValue', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasDateRangeDecrease', 'prop_class': LongProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasDateRangeIncrease', 'prop_class': LongProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasDateTimeAnswerValue', 'prop_class': DateTimeProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasDoubleAnswerValue', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasDoubleRangeDecrease', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasDoubleRangeIncrease', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasFileAnswerValueURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasHaleyAnswerComparison', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasHaleyAnswerConstantURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasHaleyAnswerConstraintComparatorURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasHaleyAnswerConstraintRelationshipURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasHaleyAnswerConstraintType', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasHaleyAnswerDataType', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasHaleyAnswerTypeComparison', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasHaleyAnswerUnitType', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasHaleyCurrencyType', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasIntegerAnswerValue', 'prop_class': IntegerProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasIntegerRangeDecrease', 'prop_class': IntegerProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasIntegerRangeIncrease', 'prop_class': IntegerProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasLongTextAnswerValue', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasLowerBoundCurrencyValue', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasLowerBoundDateValue', 'prop_class': DateTimeProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasLowerBoundDoubleValue', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasLowerBoundIntegerValue', 'prop_class': IntegerProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasMultiChoiceAnswerValue', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasMultiTaxonomyAnswerValue', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasObjectAnswerValueURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasSignatureAnswerValue', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasTaxonomyAnswerValue', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasUpperBoundCurrencyValue', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasUpperBoundDateValue', 'prop_class': DateTimeProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasUpperBoundDoubleValue', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-question#hasUpperBoundIntegerValue', 'prop_class': IntegerProperty}, 
    ]

    @classmethod
    def get_allowed_properties(cls):
        return super().get_allowed_properties() + HaleyAnswerConstraint._allowed_properties

    @classmethod
    def get_class_uri(cls) -> str:
        return 'http://vital.ai/ontology/haley-ai-question#HaleyAnswerConstraint'

