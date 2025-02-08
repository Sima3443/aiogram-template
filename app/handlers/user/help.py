from aiogram import types
from aiogram.filters import Command
from aiogram.filters.state import StateFilter

from app.routers import user_router as router
from app.handlers.msg_text import msg_text


@router.message(Command("help"), StateFilter(None))
async def _help_command(message: types.Message) -> None:
    """Дает описание бота"""
    await message.answer(msg_text.INFO)
