from aiogram.types import BotCommand, BotCommandScopeChat, BotCommandScopeDefault

from loader import bot

user_commands = [
    BotCommand("/start", "start bot"),
    BotCommand("/help", "how it works?"),
    BotCommand("/lang", "change language"),
]

admin_commands = [
    BotCommand("/admin", "example"),
]


async def set_default_commands():
    await bot.set_my_commands(user_commands, scope=BotCommandScopeDefault())


async def set_admin_commands(user_id: int):
    await bot.set_my_commands(admin_commands, scope=BotCommandScopeChat(user_id))
