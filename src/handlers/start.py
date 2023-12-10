from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup

router = Router()


@router.message(Command("start"))
async def start(message: Message):
    kb = [
        [
            KeyboardButton(text="Напоминание")
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите команду"
    )
    await message.answer("Бананы?", reply_markup=keyboard)
