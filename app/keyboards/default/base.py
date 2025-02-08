from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove,
)

from loader import _

from .kb_generator import simple_kb_generator as gen

del_kb = ReplyKeyboardRemove()

example_simple_kb = gen(["example"])


def example_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text=("example")),
            ],
        ],
        one_time_keyboard=True,
    )
    return kb
