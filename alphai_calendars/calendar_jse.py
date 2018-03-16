from datetime import time

from pandas.tseries.holiday import Holiday, weekend_to_monday, GoodFriday
from pandas.tseries.offsets import Easter, Day
from pytz import timezone

from pandas.tseries.holiday import AbstractHolidayCalendar
from pandas_market_calendars.us_holidays import USNewYearsDay

from pandas_market_calendars import MarketCalendar

MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY = range(7)


class JSEExchangeCalendar(MarketCalendar):
    """
    Exchange calendar for JSE

    Open Time: 9:00 AM, Africa/Johannesburg (GMT+2)
    Close Time: 5:00 PM, Africa/Johannesburg (GMT+2)
    """

    regular_early_close = time(13)
    lunch_start = time(11, 30)
    lunch_end = time(12, 30)

    @property
    def name(self):
        return "JSE"

    @property
    def tz(self):
        return timezone('Africa/Johannesburg')

    @property
    def open_time_default(self):
        return time(9, 0)

    @property
    def close_time_default(self):
        return time(17)

    @property
    def regular_holidays(self):
        return AbstractHolidayCalendar(rules=[
            USNewYearsDay,
            Holiday(
                name="New Year's Day",
                month=1,
                day=2,
                observance=weekend_to_monday,
            ),
            Holiday(  # 21 March
                name="Human Rights Day",
                month=1,
                day=21,
                observance=weekend_to_monday,
            ),
            GoodFriday,
            Holiday(
                name="Family Day",
                month=1,
                day=1,
                offset=[Easter(), Day(1)]
            ),
            Holiday(
                name="Freedom Day",
                month=4,
                day=27,
                observance=weekend_to_monday,
            ),
            Holiday(
                name="Workers Day",
                month=5,
                day=1,
                observance=weekend_to_monday,
            ),
            Holiday(
                name="National Women's Day",
                month=8,
                day=9,
                observance=weekend_to_monday,
            ),
            Holiday(
                name="Heritage Day",
                month=9,
                day=24,
                observance=weekend_to_monday,
            ),
            Holiday(
                name="Day of Reconciliation",
                month=12,
                day=17,
                observance=weekend_to_monday,
            ),
            # Christmas
            Holiday(
                name="Christmas",
                month=12,
                day=25,
            ),
            # If christmas day is Saturday Monday 27th is a holiday
            # If christmas day is sunday the Tuesday 27th is a holiday
            Holiday(
                "Weekend Christmas",
                month=12,
                day=27,
                days_of_week=(MONDAY, TUESDAY),
            ),
            # Boxing day
            Holiday(
                "Boxing Day",
                month=12,
                day=26,
            ),
            # If boxing day is saturday then Monday 28th is a holiday
            # If boxing day is sunday then Tuesday 28th is a holiday
            Holiday(
                "Weekend Boxing Day",
                month=12,
                day=28,
                days_of_week=(MONDAY, TUESDAY),
            )
        ])
