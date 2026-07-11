
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


class Document(VITAL_Node):
    _allowed_properties = [
        {'uri': 'http://vital.ai/ontology/vital-nlp#hasAnalyzedBody', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-nlp#hasAnalyzedTitle', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-nlp#hasBody', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-nlp#hasContentID', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-nlp#hasContentTag', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-nlp#hasDmozPath', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-nlp#hasDocumentPublicationDate', 'prop_class': DateTimeProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-nlp#hasDocumentSourceName', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-nlp#hasDocumentTitle', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-nlp#hasDocumentUrl', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-nlp#hasDocumentUrlRoot', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-nlp#hasExtractedText', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-nlp#hasExtractedTitle', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-nlp#hasLang', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-nlp#hasSentimentScore', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-nlp#hasSlug', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-nlp#hasSourceDomain', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-nlp#isSentimentMixed', 'prop_class': BooleanProperty}, 
    ]

    @classmethod
    def get_allowed_properties(cls):
        return super().get_allowed_properties() + Document._allowed_properties

    @classmethod
    def get_class_uri(cls) -> str:
        return 'http://vital.ai/ontology/vital-nlp#Document'

