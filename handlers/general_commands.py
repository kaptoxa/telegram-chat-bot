from keyboards import get_keyboard
from aiogram import types
from jedychatbot import JedyChatBot

from misc import dp, chats, get_chat


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    chat_id = message.from_user.id
    jbot = get_chat(chat_id)

    text, replies = jbot.issues()
    await message.answer(text, reply_markup=get_keyboard(replies))
