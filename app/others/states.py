from aiogram.fsm.state import State, StatesGroup


class DefaultState(StatesGroup):
    waiting = State()
