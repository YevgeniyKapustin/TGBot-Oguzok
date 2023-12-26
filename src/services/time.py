from datetime import datetime, time

from pytz import timezone


class Time(object):
    __slots__ = ('__user_time_input', '__date', '__unix_date')

    def __init__(self, user_time_input: str):
        self.__user_time_input: str = user_time_input
        self.__unix_date: int = self.__convert_str_time_to_int()

    def get_unix_time(self) -> int:
        return self.__unix_date

    def get_text_time(self) -> str:
        return self.__date

    def __convert_str_time_to_int(self) -> int:
        now: datetime = datetime.now(timezone('Europe/Moscow'))
        if ' ' in self.__user_time_input:
            date: datetime = timezone('Europe/Moscow').localize(
                datetime.strptime(self.__user_time_input, '%d %H:%M').
                replace(year=now.year).
                replace(month=now.month)
            )
        else:
            date: datetime = timezone('Europe/Moscow').localize(
                datetime.strptime(self.__user_time_input, '%H:%M').
                replace(year=now.year).
                replace(month=now.month).
                replace(day=int(get_it_next_day(
                    hour=self.__user_time_input.split(':')[0],
                    minutes=self.__user_time_input.split(':')[1]
                )))
            )

        if date < now:
            if date.month < 12:
                date: datetime = date.replace(month=date.month + 1)
            else:
                date: datetime = date.replace(year=date.year + 1)
                date: datetime = date.replace(month=date.month - 11)
        self.__date: str = date.strftime("%m.%d %H:%M")
        return int(date.timestamp())


def get_it_next_day(hour: str | int, minutes: str | int) -> str:
    now: datetime = datetime.now()
    desired_time: time = time(int(hour), int(minutes))
    return str(now.day + 1 if now.time() > desired_time else now.day)
