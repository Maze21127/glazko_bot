from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

support_cities = {
    "Москва": "https://t.me/GlazkoMoscow",
    "Санкт-Петербург": "https://t.me/glazko_spb",
    "Калининград": "https://t.me/Glazko_kld",
    "Казань": "https://t.me/glazkokzn",
    "Якутск": "https://t.me/glazkoykt"
}

BACKS = {
    "address": 'back_address',
    "promo": 'back_promo'
}

CONTACTS = {
    "address": 'contact_address',
    "promo": 'contact_promo',
    "prices": 'contact_prices'
}

BACK_TO_CITY = {
    "price_msk": "back_price_mks",
    "price_spb": "back_price_spb",
    "price_kld": "back_price_kld",
    "price_kzn": "back_price_kzn",
    "price_ykt": "back_price_ykt",
}

CONTACT_CITY = {
    "price_msk": "https://t.me/GlazkoMoscow",
    "price_spb": "https://t.me/glazko_spb",
    "price_kld": "https://t.me/Glazko_kld",
    "price_kzn": "https://t.me/glazkokzn",
    "price_ykt": "https://t.me/glazkoykt",
}


def get_links_keyboard(back_button: str):
    keyboard = InlineKeyboardMarkup(row_width=2)

    for k, v in support_cities.items():
        keyboard.insert(InlineKeyboardButton(k, url=v))

    keyboard.add(InlineKeyboardButton("🔙 Назад", callback_data=BACKS[back_button]))
    return keyboard


def get_contact_keyboard(back_button: str, city=None):
    keyboard = InlineKeyboardMarkup(row_width=2)

    if city is None:
        keyboard.add(InlineKeyboardButton("👇🏻 Связаться", callback_data=CONTACTS[back_button]))
        keyboard.add(InlineKeyboardButton("🔙 Назад", callback_data='back_start'))
    else:
        keyboard.add(InlineKeyboardButton("👇🏻 Связаться", url=CONTACT_CITY[city]))
        keyboard.add(InlineKeyboardButton("🔙 Назад", callback_data=BACK_TO_CITY[city]))
    return keyboard
