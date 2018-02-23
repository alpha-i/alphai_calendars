from alphai_calendars.calendar_gym_uk import GymUkCalendar

_calendars = {
    'GYMUK': GymUkCalendar,

}

_aliases = {
    'gym_uk': 'GYMUK',
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
