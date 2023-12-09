from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.text.lower() == "отложенное сообщение")
async def delayed_message(message: Message):
    await message.reply("Отличный выбор!")
