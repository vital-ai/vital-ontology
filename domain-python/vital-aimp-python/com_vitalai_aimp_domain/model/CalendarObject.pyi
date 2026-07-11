
import datetime
from com_vitalai_aimp_domain.model.Card import Card


class CalendarObject(Card):
        calendars: str
        endDate: datetime
        startDate: datetime

