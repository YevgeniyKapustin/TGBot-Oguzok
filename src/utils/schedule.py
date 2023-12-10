from asyncio import sleep

from aiogram.types import Message
from loguru import logger


async def send_delayed_message(message: Message, delay: int) -> None:
    logger.info(f'send the message with id {message.message_id} in {delay}s')
    await sleep(int(delay))
    logger.info(f'reply the message with id {message.message_id} now')
    await message.reply(text='🔔')
