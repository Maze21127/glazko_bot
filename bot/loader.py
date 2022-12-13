from aiogram import Bot, Dispatcher, types

from app.settings import BOT_TOKEN

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
