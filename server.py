#part for telegram bot
import logging

from aiogram import Bot, Dispatcher, executor, md, types
from misc import bot, storage, dp, posts_cb
import handlers


if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)
