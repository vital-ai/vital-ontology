
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyWeatherReport(VITAL_Node):
        airQualityIrradiance: float
        airQualityOzone: float
        airQualityUltraVioletIndex: float
        haleyWeatherMoonPhaseURI: str
        haleyWeatherWindCompassDirectionURI: str
        weatherAirPressure: float
        weatherCloudCover: float
        weatherDewPoint: float
        weatherElevation: float
        weatherFeelsLikeTemperature: float
        weatherHumidity: float
        weatherMoonRise: datetime
        weatherMoonSet: datetime
        weatherPrecipitationTotal: float
        weatherPrecipitationType: str
        weatherReportDateTime: datetime
        weatherReportIcon: str
        weatherReportIconInteger: int
        weatherReportJSON: str
        weatherReportLatitude: float
        weatherReportLongitude: float
        weatherReportSummary: str
        weatherReportTimeZoneIdentifier: str
        weatherReportUnits: str
        weatherSunrise: datetime
        weatherSunset: datetime
        weatherTemperature: float
        weatherVisibility: float
        weatherWindChill: float
        windAngle: float
        windDirection: str
        windSpeed: float
        weatherReportHistorical: bool

