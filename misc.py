import logging

import os
from jedychatbot import JedyChatBot

from aiogram import Bot, Dispatcher, executor, md, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils.callback_data import CallbackData
from middlewares import AccessMiddleware


logging.basicConfig(level=logging.INFO)

API_TOKEN = os.getenv('API_TOKEN')

bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())

ACCESS_IDs = os.getenv("TELEGRAM_ACCESS_IDS")
dp.middleware.setup(AccessMiddleware(ACCESS_IDs))

posts_cb = CallbackData('post', 'id', 'action')  # post:<id>:<action>

chats = {}
def get_chat(chat_id):
    if chat_id not in chats:
        chats[chat_id] = JedyChatBot(chat_id)
    return chats[chat_id]
