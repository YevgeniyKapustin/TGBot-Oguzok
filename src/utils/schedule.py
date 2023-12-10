from asyncio import sleep


async def send_delayed_message(message, delay):
    await sleep(int(delay))
    await message.reply(text='🔔')
