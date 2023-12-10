from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from loguru import logger

router = Router()


@router.message(Command("start"))
async def start(message: Message):
    keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Напоминание")]],
        resize_keyboard=True,
        input_field_placeholder="Выберите команду"
    )
    logger.info(f'new user: {message.chat.username}')
    await message.answer("Бананы?", reply_markup=keyboard)
