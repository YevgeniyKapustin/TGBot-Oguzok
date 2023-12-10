import logging

from aiogram import Bot, Dispatcher

from src import config
from src.handlers import start, reminder


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(config.TOKEN)
    dp = Dispatcher()
    dp.include_routers(
        start.router,
        reminder.router,
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
