from aiogram.fsm.state import StatesGroup, State


class Reminder(StatesGroup):
    choosing_time: State = State()
    choosing_message: State = State()
