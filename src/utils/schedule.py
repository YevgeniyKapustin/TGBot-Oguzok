from asyncio import sleep

from aiogram.types import Message


async def send_delayed_message(message: Message, delay: int) -> None:
    await sleep(int(delay))
    await message.reply(text='🔔')
