from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


FEEDBACK_CITIES = {
    "Москва": "feedback_msk",
    "Санкт-Петербург": "feedback_spb",
    "Калининград": "feedback_kld",
    "Казань": "feedback_kzn",
    "Якутск": "feedback_ykt"
}

FEEDBACK_KEYBOARD = InlineKeyboardMarkup(row_width=2)

for k, v in FEEDBACK_CITIES.items():
    FEEDBACK_KEYBOARD.insert(InlineKeyboardButton(k, callback_data=v))

FEEDBACK_KEYBOARD.add(InlineKeyboardButton("🔙 Назад", callback_data='back_start'))


BACK_CITIES = {
    "feedback_msk": "back_feedback_msk",
    "feedback_spb": "back_feedback_spb",
    "feedback_kld": "back_feedback_kld",
    "feedback_kzn": "back_feedback_kzn",
    "feedback_ykt": "back_feedback_ykt",
}


def get_feedback_for_city(city: str, links: list):
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.insert(InlineKeyboardButton("Яндекс", url=links[0]))
    keyboard.insert(InlineKeyboardButton("Google", url=links[1]))
    keyboard.insert(InlineKeyboardButton("2ГИС", url=links[2]))

    keyboard.add(InlineKeyboardButton("🔙 Назад", callback_data=BACK_CITIES[city]))
    return keyboard
