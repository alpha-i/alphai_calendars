import calendar
import datetime
from dateutil.relativedelta import relativedelta
from pandas_market_calendars.market_calendar import clean_dates

from alphai_calendars.calendar_jse import JSEExchangeCalendar

DATE_STRING = '%Y-%m-%d'

MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY = range(7)


class JSEEOMCalendar(JSEExchangeCalendar):
    """
    Exchange calendar for JSE

    Open Time: 9:00 AM, Africa/Johannesburg (GMT+2)
    Close Time: 5:00 PM, Africa/Johannesburg (GMT+2)
    """

    @property
    def name(self):
        return "JSEEOM"

    def schedule(self, start_date, end_date):
        # shift to the first day of the next month
        start_date, end_date = clean_dates(start_date, end_date)
        end_date = end_date + relativedelta(months=1)
        schedule = super().schedule(start_date, end_date)

        current_day = schedule.index[0]
        selected_days = []
        for date_index in schedule.index[1:]:
            if date_index.month != current_day.month:
                selected_days.append(current_day)
            current_day = date_index

        return schedule.loc[selected_days]




