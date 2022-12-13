from aiogram import types

from bot.api import get_message
from bot.keyboards.contact import get_links_keyboard, get_contact_keyboard
from bot.loader import dp


@dp.callback_query_handler(lambda cb: cb.data == 'address')
async def support(callback_query: types.CallbackQuery):
    answer = await get_message('addresses_message')
    await callback_query.message.edit_text(answer)
    return await callback_query.message.edit_reply_markup(reply_markup=get_contact_keyboard('address'))


@dp.callback_query_handler(lambda cb: cb.data == 'contact_address')
async def support(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text("Выбери город:")
    return await callback_query.message.edit_reply_markup(reply_markup=get_links_keyboard('address'))


@dp.callback_query_handler(lambda cb: cb.data == 'back_address')
async def support(callback_query: types.CallbackQuery):
    answer = await get_message('addresses_message')
    await callback_query.message.edit_text(answer)
    return await callback_query.message.edit_reply_markup(reply_markup=get_contact_keyboard('address'))
