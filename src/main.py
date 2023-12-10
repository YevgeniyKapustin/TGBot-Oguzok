import asyncio

from aiogram import Bot, Dispatcher
from loguru import logger

from src import config
from src.handlers import start, reminder


async def main() -> None:
    logger.info('launch...')
    try:
        bot: Bot = Bot(config.TOKEN)
        dp: Dispatcher = Dispatcher()
        dp.include_routers(
            start.router,
            reminder.router,
        )
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as exception:
        logger.critical(exception)
