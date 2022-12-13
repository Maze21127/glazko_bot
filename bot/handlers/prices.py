from aiogram import types

from bot.api import get_message
from bot.keyboards.contact import get_contact_keyboard, BACK_TO_CITY
from bot.keyboards.prices import PRICES_KEYBOARD, PRICES_CITIES
from bot.loader import dp


@dp.callback_query_handler(lambda cb: cb.data == 'prices')
async def support(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text("Выбери город:")
    return await callback_query.message.edit_reply_markup(reply_markup=PRICES_KEYBOARD)


@dp.callback_query_handler(lambda cb: cb.data in PRICES_CITIES.values())
async def support(callback_query: types.CallbackQuery):
    city = callback_query.data
    answer = await get_message(f"{city}_message")
    await callback_query.message.edit_text(answer)
    return await callback_query.message.edit_reply_markup(reply_markup=get_contact_keyboard('prices', city))


@dp.callback_query_handler(lambda cb: cb.data in BACK_TO_CITY.values())
async def support(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text("Выбери город:")
    return await callback_query.message.edit_reply_markup(reply_markup=PRICES_KEYBOARD)
