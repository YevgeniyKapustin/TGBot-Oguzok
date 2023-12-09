from aiogram.fsm.state import StatesGroup, State


class Reminder(StatesGroup):
    choosing_time = State()
    choosing_message = State()
