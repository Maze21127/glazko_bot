from aiogram import executor, Dispatcher
from bot.loader import dp


async def on_startup(dispatcher: Dispatcher):
    print("Bot starting...")

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
