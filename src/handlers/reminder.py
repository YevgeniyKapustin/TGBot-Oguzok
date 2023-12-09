from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.services.messages import reminder_step1, reminder_step2
from src.services.reminder import Reminder

router = Router()


@router.message(StateFilter(None), F.text.lower() == "напоминание")
async def reminder(message: Message, state: FSMContext):
    await message.reply(reminder_step1)
    await state.set_state(Reminder.choosing_time)


@router.message(Reminder.choosing_time)
async def time_chosen(message: Message, state: FSMContext):
    await state.update_data(choosing_time=message.text.lower())
    await message.answer(reminder_step2)
    await state.set_state(Reminder.choosing_message)


@router.message(StateFilter("Reminder:choosing_time"))
async def time_chosen_incorrectly(message: Message):
    await message.reply(text='Не корректно указана дата')


@router.message(Reminder.choosing_message)
async def message_chosen(message: Message, state: FSMContext):
    await state.update_data(choosing_message=message.text)
    user_data = await state.get_data()
    await message.answer(
        text=f"Напоминание на {user_data['choosing_time']} установлено."
    )
    await state.clear()
