import pandas_market_calendars as mcal
from alphai_calendars.calendar_utils import get_calendar as _get_calendar


def get_calendar(calendar_name):

    calendar = mcal.get_calendar(calendar_name)
    if not calendar:
        calendar = _get_calendar(calendar_name)

    return calendar
