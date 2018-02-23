#
# Copyright 2016 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import time
from pandas.tseries.holiday import (
    Holiday,
    weekend_to_monday
)
from pytz import timezone
from pandas.tseries.holiday import AbstractHolidayCalendar
from pandas_market_calendars.market_calendar import (
    MarketCalendar
)

# New Year's Day
NewYearDay = Holiday(
    "New Year's Day",
    month=1,
    day=1,
    observance=weekend_to_monday,
)

# Christmas
Christmas = Holiday(
    "Christmas",
    month=12,
    day=25,
)


class GymUkCalendar(MarketCalendar):
    """
    United Kingdom Working Days
    (Basically all days excluding holidays)


    Regularly-Observed Holidays:
    - New Years Day (observed on first business day on/after)
    - Christmas Day
    """

    @property
    def name(self):
        return "WUK"

    @property
    def tz(self):
        return timezone('Europe/London')

    @property
    def open_time_default(self):
        return time(7, 0, tzinfo=self.tz)

    @property
    def close_time_default(self):
        return time(22, 0, tzinfo=self.tz)

    @property
    def regular_holidays(self):
        return AbstractHolidayCalendar(rules=[
            NewYearDay,
            Christmas,
        ])

    @property
    def special_closes(self):
        return []
