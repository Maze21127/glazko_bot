from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

PROMO_KEYBOARD = InlineKeyboardMarkup(row_width=2)

PROMO_KEYBOARD.add(InlineKeyboardButton("👇🏻 Связаться", callback_data='contact_promo'))
PROMO_KEYBOARD.add(InlineKeyboardButton("🔙 Назад", callback_data='back_start'))
