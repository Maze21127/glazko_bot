from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


PRICES_CITIES = {
    "Москва": "price_msk",
    "Санкт-Петербург": "price_spb",
    "Калининград": "price_kld",
    "Казань": "price_kzn",
    "Якутск": "price_ykt"
}

PRICES_KEYBOARD = InlineKeyboardMarkup(row_width=2)

for k, v in PRICES_CITIES.items():
    PRICES_KEYBOARD.insert(InlineKeyboardButton(k, callback_data=v))

PRICES_KEYBOARD.add(InlineKeyboardButton("🔙 Назад", callback_data='back_start'))
