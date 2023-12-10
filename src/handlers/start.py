from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup

router = Router()


@router.message(Command("start"))
async def start(message: Message):
    keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Напоминание")]],
        resize_keyboard=True,
        input_field_placeholder="Выберите команду"
    )
    await message.answer("Бананы?", reply_markup=keyboard)
