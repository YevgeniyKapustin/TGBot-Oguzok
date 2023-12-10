from datetime import datetime


class Time(object):
    __user_time_input: str
    __date: datetime
    __unix_date: int

    def __init__(self, user_time_input: str):
        self.__user_time_input = user_time_input
        self.__unix_date = self.__convert_str_time_to_int()

    def get_unix_time(self):
        return self.__unix_date

    def get_text_time(self):
        return self.__date

    def __convert_str_time_to_int(self):
        now = datetime.now()
        date = (
            datetime.strptime(self.__user_time_input, "%d %H:%M").
            replace(year=now.year).
            replace(month=now.month)
        )

        if date < now:
            if date.month < 12:
                date = date.replace(month=date.month + 1)
            else:
                date = date.replace(year=date.year + 1)
                date = date.replace(month=date.month - 11)
        self.__date = date
        return int(date.timestamp())
