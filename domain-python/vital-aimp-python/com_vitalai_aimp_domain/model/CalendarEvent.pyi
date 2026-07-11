
import datetime
from com_vitalai_aimp_domain.model.AIMPThing import AIMPThing


class CalendarEvent(AIMPThing):
        calendarURI: str
        endDate: datetime
        locationString: str
        shortDescription: str
        startDate: datetime
        fullDayEvent: bool

