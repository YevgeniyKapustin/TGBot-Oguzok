from datetime import datetime

from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.services.reminder import Reminder
from src.utils.filtres import ReminderTimeFilter
from src.utils.schedule import send_delayed_message
from src.services.time import Time

router = Router()


@router.message(StateFilter(None), F.text.lower() == "напоминание")
async def reminder(message: Message, state: FSMContext):
    await message.reply(
        'Напиши время, в которое необходимо напомнить о заметке. '
        'Например: "27 16:40" (день час:минуты)'
    )
    await state.set_state(Reminder.choosing_time)


@router.message(Reminder.choosing_time, ReminderTimeFilter())
async def time_chosen(message: Message, state: FSMContext):
    await state.update_data(choosing_time=message.text.lower())
    await message.answer('ТЕПЕПЬ НАПИШИ САМО НАПОМИНАНИЕ СУКА.')
    await state.set_state(Reminder.choosing_message)


@router.message(StateFilter("Reminder:choosing_time"))
async def time_chosen_incorrectly(message: Message):
    await message.reply(text='Не корректно указана дата')


@router.message(Reminder.choosing_message)
async def message_chosen(message: Message, state: FSMContext):
    user_data = await state.get_data()
    time = Time(user_data['choosing_time'])
    await message.answer(
        text=f'Напоминание на {time.get_text_time()} установлено.'
    )
    await state.clear()
    await send_delayed_message(
        message,
        time.get_unix_time() - int(datetime.now().timestamp()),
    )
