from asyncio import sleep


async def send_delayed_message(message, delay, text):
    await sleep(int(delay))
    await message.answer(text=text)
