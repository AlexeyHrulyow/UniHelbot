#navigation.py

from typing import Dict, List, Optional, Tuple

from aiofiles.os import remove
from aiogram.types import InlineKeyboardMarkup


class Navigation:
    def __init__(self):
        self.history: Dict[int, list[Tuple[str, InlineKeyboardMarkup]]] = {}

    def push(self, user_id: int, text: str, keyboard: InlineKeyboardMarkup):
        if user_id not in self.history:
            self.history[user_id] = []

            if self.history[user_id] and self.history[user_id][-1] == (text, keyboard):
                return

        self.history[user_id].append((text, keyboard))
        if len(self.history[user_id]) > 5:
            del self.history[user_id][0]
        pass

    def pop(self, user_id: int):
        if user_id in self.history and self.history[user_id]:
            return self.history[user_id].pop()  # Удалить и вернуть последний элемент
        return None

    def clear(self, user_id: int):
        if user_id in self.history:
            self.history[user_id].clear()