from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove,
)
from loader import _

from .kb_generator import simple_kb_generator as kb_gen


del_kb = ReplyKeyboardRemove()


def base_kb():
    kb = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text="click"),
            ],
        ],
    )
    return kb


"""Пример более компактных простых клавиатур"""
example_kb: ReplyKeyboardMarkup = kb_gen(["click"])
