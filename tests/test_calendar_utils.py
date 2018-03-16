from datetime import datetime

import pytz

from alphai_calendars import get_calendar


def test_get_minutes_in_one_day():

    jpx_calendar = get_calendar('JPX')
    assert jpx_calendar.get_minutes_in_one_day() == 360

    nyse_calendar = get_calendar('NYSE')
    assert nyse_calendar.get_minutes_in_one_day() == 390

    gymuk_calendar = get_calendar('GYMUK')
    assert gymuk_calendar.get_minutes_in_one_day() == 900

    jse_calendar = get_calendar('JSE')
    assert jse_calendar.get_minutes_in_one_day() == 480


def test_closing_time_for_day():

    the_day = datetime(2016, 5, 10, tzinfo=pytz.utc)
    jpx_calendar = get_calendar('JPX')
    closing_time = jpx_calendar.closing_time_for_day(the_day)

    assert closing_time == the_day.replace(hour=6)

    the_day = datetime(2016, 5, 10, tzinfo=pytz.utc)
    nyse_calendar = get_calendar('NYSE')
    closing_time = nyse_calendar.closing_time_for_day(the_day)

    assert closing_time == the_day.replace(hour=20)

    gym_uk = get_calendar('GYMUK')
    closing_time = gym_uk.closing_time_for_day(the_day)

    assert closing_time == the_day.replace(hour=21)

    JSE = get_calendar('JSE')
    closing_time = JSE.closing_time_for_day(the_day)

    assert closing_time == the_day.replace(hour=15)
