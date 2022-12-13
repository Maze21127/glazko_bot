from bot.api import get_message
from bot.keyboards.contact import get_contact_keyboard
from bot.keyboards.start import BACK_TO_MENU_KEYBOARD, get_start_keyboard

from bot.loader import dp
from aiogram import types


@dp.message_handler(commands=['start'], state="*")
async def start(message: types.Message):
    answer = await get_message('start_message')
    return await message.answer(answer, reply_markup=get_start_keyboard({
        "sight": await get_message('sight_channel_link'),
        "frames_catalog": await get_message('frames_catalog_link')
    }))


@dp.callback_query_handler(lambda cb: cb.data == 'back_start')
async def back_start(callback_query: types.CallbackQuery):
    answer = await get_message('start_message')
    await callback_query.message.edit_text(answer)
    return await callback_query.message.edit_reply_markup(reply_markup=get_start_keyboard({
        "sight": await get_message('sight_channel_link'),
        "frames_catalog": await get_message('frames_catalog_link')
    }))


@dp.callback_query_handler(lambda cb: cb.data in ('faq', 'promo)'))
async def faq(callback_query: types.CallbackQuery):
    if callback_query.data == 'faq':
        answer = await get_message('faq_message')
        await callback_query.message.edit_text(answer)
        return await callback_query.message.edit_reply_markup(reply_markup=BACK_TO_MENU_KEYBOARD)
    elif callback_query.data == 'promo':
        answer = await get_message('promo_message')
        await callback_query.message.edit_text(answer)
        return await callback_query.message.edit_reply_markup(reply_markup=get_contact_keyboard('promo'))
