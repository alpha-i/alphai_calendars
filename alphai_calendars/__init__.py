import pandas_market_calendars as mcal

from alphai_calendars.calendar_utils import get_calendar as alphai_get_calendar, EnhancedCalendar


def get_calendar(calendar_name):

    try:
        calendar = alphai_get_calendar(calendar_name)
    except KeyError as e:
        calendar = mcal.get_calendar(calendar_name)

    return EnhancedCalendar(calendar)
