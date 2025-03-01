from aiogram import BaseMiddleware
from aiogram.types import Message

from database.service.users import create_user, get_user, new_referral

from utils.base62 import decode_base62

from typing import Any, Callable


class StartMiddleware(BaseMiddleware):
    async def __call__(self, handler: Callable, message: Message, data: dict) -> Any:
        if user := await get_user(message.from_user.id):
            if not user.is_banned:
                data["user"] = user
                return await handler(message, data)
            return

        user = await create_user(
            user_id=message.from_user.id,
            username=message.from_user.username,
            language=message.from_user.language_code,
        )
        data["user"] = user

        if inviter := data["command"].args:
            await new_referral(decode_base62(inviter))

        return await handler(message, data)
