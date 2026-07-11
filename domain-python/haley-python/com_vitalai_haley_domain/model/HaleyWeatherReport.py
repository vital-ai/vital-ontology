
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


class HaleyWeatherReport(VITAL_Node):
    _allowed_properties = [
        {'uri': 'http://vital.ai/ontology/haley#hasAirQualityIrradiance', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasAirQualityOzone', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasAirQualityUltraVioletIndex', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasHaleyWeatherMoonPhaseURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasHaleyWeatherWindCompassDirectionURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasWeatherAirPressure', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasWeatherCloudCover', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasWeatherDewPoint', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasWeatherElevation', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasWeatherFeelsLikeTemperature', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasWeatherHumidity', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasWeatherMoonRise', 'prop_class': DateTimeProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasWeatherMoonSet', 'prop_class': DateTimeProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasWeatherPrecipitationTotal', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasWeatherPrecipitationType', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasWeatherReportDateTime', 'prop_class': DateTimeProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasWeatherReportIcon', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasWeatherReportIconInteger', 'prop_class': IntegerProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasWeatherReportJSON', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasWeatherReportLatitude', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasWeatherReportLongitude', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasWeatherReportSummary', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasWeatherReportTimeZoneIdentifier', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasWeatherReportUnits', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasWeatherSunrise', 'prop_class': DateTimeProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasWeatherSunset', 'prop_class': DateTimeProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasWeatherTemperature', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasWeatherVisibility', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasWeatherWindChill', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasWindAngle', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasWindDirection', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#hasWindSpeed', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/haley#isWeatherReportHistorical', 'prop_class': BooleanProperty}, 
    ]

    @classmethod
    def get_allowed_properties(cls):
        return super().get_allowed_properties() + HaleyWeatherReport._allowed_properties

    @classmethod
    def get_class_uri(cls) -> str:
        return 'http://vital.ai/ontology/haley#HaleyWeatherReport'

