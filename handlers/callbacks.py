from keyboards import get_keyboard
from aiogram import types
from jedychatbot import JedyChatBot

from misc import bot, dp, posts_cb, get_chat


@dp.callback_query_handler(posts_cb.filter(action='view'))
async def query_view(query: types.CallbackQuery, callback_data: dict):
    post_id = int(callback_data['id'])
    chat_id = query.from_user.id
    jbot = get_chat(chat_id)

    jbot.set_state(post_id)
    text, answers = jbot.issues()

    if answers:
        markup = get_keyboard(answers)
        await query.message.edit_text(text, reply_markup=markup)
