
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
from com_vitalai_aimp_domain.model.AIMPMessage import AIMPMessage


class AnswerUnsetMessage(AIMPMessage):
    _allowed_properties = [
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasDialogPageURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasSlackChannelID', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasSlackEventType', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasSlackTeamID', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasSlackThreadID', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#hasSlackUserID', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#isAnswerSkipped', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#isGoBackSelected', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#isHelpRequested', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#isQuestionClosed', 'prop_class': BooleanProperty}, 
        {'uri': 'http://vital.ai/ontology/vital-aimp#isSlackResponse', 'prop_class': BooleanProperty}, 
    ]

    @classmethod
    def get_allowed_properties(cls):
        return super().get_allowed_properties() + AnswerUnsetMessage._allowed_properties

    @classmethod
    def get_class_uri(cls) -> str:
        return 'http://vital.ai/ontology/vital-aimp#AnswerUnsetMessage'

