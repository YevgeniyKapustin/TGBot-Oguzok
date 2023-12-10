from aiogram.filters import Filter
from aiogram.types import Message


class ReminderTimeFilter(Filter):
    async def __call__(self, message: Message) -> bool:
        if ' ' in message.text and ':' in message.text:
            day: str = message.text.split(' ')[0]
            hour: str = message.text.split(' ')[1].split(':')[0]
            minutes: str = message.text.split(' ')[1].split(':')[1]
            if day.isdigit() and hour.isdigit() and minutes.isdigit():
                if int(day) < 32 and int(hour) < 25 and int(minutes) < 61:
                    return True
        return False
