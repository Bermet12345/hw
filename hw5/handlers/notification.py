import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot


async def payment():
    ADMIN_ID = '724376781'
    await bot.send_message(
        chat_id=ADMIN_ID,
        text='Cделай дз!!'
    )


async def schedular():
    aioschedule.every().friday.at('12:00').do(payment)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)

