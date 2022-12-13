from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_start_keyboard(links: dict):

    keyboard = InlineKeyboardMarkup(row_width=2)

    support_btn = InlineKeyboardButton(f"☎️ Поддержка", callback_data='support')
    faq_btn = InlineKeyboardButton(f"❓ FAQ", callback_data='faq')
    keyboard.row(support_btn, faq_btn)

    address_btn = InlineKeyboardButton(f"📍 Узнать адрес", callback_data='address')
    promo_btn = InlineKeyboardButton(f"⚡️ Акции", callback_data='promo')
    keyboard.row(address_btn, promo_btn)

    keyboard.add(InlineKeyboardButton(f"💳 Стоимость услуг", callback_data='prices'))
    keyboard.add(InlineKeyboardButton(f"👥 Отзывы", callback_data='feedback'))

    channel1 = InlineKeyboardButton(f"Канал про зрение", url=links["sight"])
    channel2 = InlineKeyboardButton(f"Каталог оправ", url=links['frames_catalog'])
    keyboard.row(channel1, channel2)

    return keyboard


BACK_TO_MENU_KEYBOARD = InlineKeyboardMarkup().add(InlineKeyboardButton("🔙 Назад", callback_data='back_start'))
