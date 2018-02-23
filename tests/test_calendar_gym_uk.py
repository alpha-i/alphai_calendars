import pandas as pd
import pytz

from alphai_calendars.calendar_gym_uk import GymUkCalendar


def test_time_zone():
    assert GymUkCalendar().tz == pytz.timezone('Europe/London')


def test_2016_holidays():
    # 2016/01/01 - New Years Day (observed on first business day on/after)

    gym_uk = GymUkCalendar()
    good_dates = gym_uk.valid_days('2016-01-01', '2016-12-31')
    for date in ["2016-01-01", '2016-12-25']:
        assert pd.Timestamp(date, tz='UTC') not in good_dates
