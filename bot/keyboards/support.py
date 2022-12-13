from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

support_cities = {
    "Москва": "https://t.me/GlazkoMoscow",
    "Санкт-Петербург": "https://t.me/glazko_spb",
    "Калининград": "https://t.me/Glazko_kld",
    "Казань": "https://t.me/glazkokzn",
    "Якутск": "https://t.me/glazkoykt"
}

SUPPORT_KEYBOARD = InlineKeyboardMarkup(row_width=2)

for k, v in support_cities.items():
    SUPPORT_KEYBOARD.insert(InlineKeyboardButton(k, url=v))

SUPPORT_KEYBOARD.add(InlineKeyboardButton("🔙 Назад", callback_data='back_start'))
