#states.py

from aiogram.fsm.state import State, StatesGroup


class ReceiptStates(StatesGroup):
    waiting_photo = State()
    photo_processing = State()
