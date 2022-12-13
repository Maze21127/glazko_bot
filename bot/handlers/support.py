from aiogram import types

from bot.keyboards.support import SUPPORT_KEYBOARD
from bot.loader import dp


@dp.callback_query_handler(lambda cb: cb.data == 'support')
async def support(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text("Выбери город:")
    return await callback_query.message.edit_reply_markup(reply_markup=SUPPORT_KEYBOARD)

