from aiogram import types

from bot.api import get_message
from bot.keyboards.feedback import FEEDBACK_KEYBOARD, FEEDBACK_CITIES, get_feedback_for_city, BACK_CITIES
from bot.loader import dp


@dp.callback_query_handler(lambda cb: cb.data == 'feedback')
async def support(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text("Выбери город:")
    return await callback_query.message.edit_reply_markup(reply_markup=FEEDBACK_KEYBOARD)


@dp.callback_query_handler(lambda cb: cb.data in FEEDBACK_CITIES.values())
async def support(callback_query: types.CallbackQuery):
    city = callback_query.data
    links = [
        await get_message(f'{city}_yandex'),
        await get_message(f'{city}_google'),
        await get_message(f'{city}_2gis')
    ]
    await callback_query.message.edit_text("Отзывы")
    return await callback_query.message.edit_reply_markup(reply_markup=get_feedback_for_city(city, links))


@dp.callback_query_handler(lambda cb: cb.data in BACK_CITIES.values())
async def support(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text("Выбери город:")
    return await callback_query.message.edit_reply_markup(reply_markup=FEEDBACK_KEYBOARD)
