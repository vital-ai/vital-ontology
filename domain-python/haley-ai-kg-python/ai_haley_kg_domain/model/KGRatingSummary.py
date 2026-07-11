
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
from ai_haley_kg_domain.model.KGNode import KGNode


class KGRatingSummary(KGNode):
    _allowed_properties = [
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGRatingCalculationDateTime', 'prop_class': DateTimeProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGRatingSummaryAverageRatingDouble', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGRatingSummaryAverageStarRating', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGRatingSummaryNegativeCount', 'prop_class': LongProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGRatingSummaryNeutralCount', 'prop_class': LongProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGRatingSummaryPositiveCount', 'prop_class': LongProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGRatingSummaryReviewCount', 'prop_class': IntegerProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGRatingSummaryText', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGRatingSummaryTitle', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGRatingSummaryTotalCount', 'prop_class': LongProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGRatingSummaryType', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley-ai-kg#hasKGRatingValueTypeURI', 'prop_class': URIProperty}, 
    ]

    @classmethod
    def get_allowed_properties(cls):
        return super().get_allowed_properties() + KGRatingSummary._allowed_properties

    @classmethod
    def get_class_uri(cls) -> str:
        return 'http://vital.ai/ontology/haley-ai-kg#KGRatingSummary'

