"""Аутентификация — пропускаем сообщения только от одного Telegram аккаунта"""
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware


class AccessMiddleware(BaseMiddleware):
    def __init__(self, access_ids: int):
        self.access_ids = set(int(id) for id in access_ids.split())
        super().__init__()

    async def on_pre_process_message(self, message: types.ContentType.DOCUMENT, _):
        if message.document:
            if int(message.from_user.id) not in self.access_ids: 
                await message.answer("Access Denied")
                raise CancelHandler()
