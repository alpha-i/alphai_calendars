import datetime
from collections import namedtuple

import pandas as pd
from pandas_market_calendars import MarketCalendar

from alphai_calendars.calendar_gym_uk import GymUkCalendar

ROOM_FOR_SCHEDULE = 10

MarketDay = namedtuple('MarketDay', 'open close')

_calendars = {
    'GYMUK': GymUkCalendar,

}

_aliases = {
    'GYMUK': 'GYMUK',
}


def get_calendar(name, open_time=None, close_time=None):
    """
    Retrieves an instance of an MarketCalendar whose name is given.
    :param name: The name of the MarketCalendar to be retrieved.
    :param open_time: Market open time override as datetime.time object. If None then default is used.
    :param close_time: Market close time override as datetime.time object. If None then default is used.
    :return: MarketCalendar of the desired calendar.
    """
    canonical_name = _aliases.get(name, name)
    return _calendars[canonical_name](open_time, close_time)


class EnhancedCalendar:
    """
    Decorator Pattern Class to add new functionality to a pandas market calendar calendar
    """
    def __init__(self, calendar):
        self.calendar = calendar

    @property
    def name(self):
        return self.calendar.name

    @property
    def tz(self):
        return self.calendar.tz

    @property
    def open_time_default(self):
        return self.calendar.open_time_default

    @property
    def close_time_default(self):
        return self.calendar.close_time_default

    @property
    def regular_holidays(self):
        return self.calendar.regular_holidays

    @property
    def adhoc_holidays(self):
        return self.calendar.adhoch_holidays

    @property
    def special_opens(self):
        return self.calendar.special_opens

    @property
    def special_opens_adhoc(self):
        return self.calendar.special_opens.adhoc

    @property
    def special_closes(self):
        return self.calendar.special_closes

    @property
    def special_closes_adhoc(self):
        return self.calendar.special_closes_adhoc

    @property
    def open_time(self):
        return self.calendar.open_time

    @property
    def close_time(self):
        return self.calendar.close_time

    @property
    def open_offset(self):
        return self.calendar.open_offset

    @property
    def close_offset(self):
        return self.calendar.close_offset

    def holidays(self):
        return self.calendar.holidays

    def valid_days(self, start_date, end_date, tz='UTC'):
        return self.calendar.valid_days(start_date, end_date, tz)

    def schedule(self, start_date, end_date):
        return self.calendar.schedule(start_date, end_date)

    @staticmethod
    def open_at_time(schedule, timestamp, include_close=False):
        return MarketCalendar.open_at_time(schedule, timestamp, include_close)

    def early_closes(self, schedule):
        return self.calendar.early_closes(schedule)

    def closing_time_for_day(self, the_day):
        """
        Given a day, it returns the market closing time
        """
        try:
            market_close = self.calendar.schedule(the_day, the_day)['market_close']
        except Exception as e:
            return None

        return pd.to_datetime(market_close).iloc[0]

    @staticmethod
    def calculate_target_day(market_schedule, prediction_day, target_delta_days):
        """
        :param market_schedule:
        :type market_schedule: pd.DataFrame (index=Timestamp, columns=['market_close','market_open'])
        :param prediction_day:
        :type prediction_day: datetime.Date
        :param target_delta_days:
        :type target_delta_days: int

        :return:
        """

        target_index = market_schedule.index.get_loc(prediction_day) + target_delta_days

        try:
            day_schedule = market_schedule.iloc[target_index]
            return MarketDay(day_schedule['market_open'], day_schedule['market_close'])
        except KeyError:
            return None

    def get_minutes_in_one_trading_day(self, exclude_lunch_break=False):
        """
        :param exclude_lunch_break: whether to discard minutes during lunch break (for Tokyo)
        :return: minutes in one trading day for the selected exchange
        :rtype: int
        """
        open_time = self.calendar.open_time
        close_time = self.calendar.close_time

        hours = close_time.hour - open_time.hour
        minutes = close_time.minute - open_time.minute

        open_interval = datetime.timedelta(hours=hours, minutes=minutes)

        lunch_break = datetime.timedelta(minutes=0)
        if exclude_lunch_break and (
                hasattr(self.calendar, 'lunch_start') and hasattr(self.calendar, 'lunch_end')):
            lunch_break = datetime.timedelta(
                hours=self.calendar.lunch_end.hour - self.calendar.lunch_start.hour,
                minutes=self.calendar.lunch_end.minute - self.calendar.lunch_start.minute
            )

        return (open_interval - lunch_break).seconds / 60
