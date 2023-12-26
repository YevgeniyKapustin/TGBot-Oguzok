from aiogram.filters import Filter
from aiogram.types import Message

from src.services.time import get_it_next_day


class ReminderTimeFilter(Filter):

    async def __call__(self, message: Message) -> bool:
        if ' ' not in message.text and ':' in message.text:
            hour: str = message.text.split(':')[0]
            minutes: str = message.text.split(':')[1]
            day: str = get_it_next_day(hour, minutes)
            return self.__check_isdigit_time(day, hour, minutes)

        elif ' ' in message.text and ':' in message.text:
            hour: str = message.text.split(' ')[1].split(':')[0]
            minutes: str = message.text.split(' ')[1].split(':')[1]
            day: str = message.text.split(' ')[0]
            return self.__check_isdigit_time(day, hour, minutes)

        return False

    @staticmethod
    def __check_isdigit_time(day: str, hour: str, minutes: str) -> bool:
        if day.isdigit() and hour.isdigit() and minutes.isdigit():
            if int(day) < 32 and int(hour) < 25 and int(minutes) < 61:
                return True
        return False
