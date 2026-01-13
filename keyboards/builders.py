#buiders.py

from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_start_menu():
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text = "Меню", callback_data = "menu"),
    )
    builder.adjust(2)
    return builder.as_markup()

def get_main_menu():
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="📊 Статистика", callback_data="stats"),
        InlineKeyboardButton(text="📸 Отправить чек", callback_data="upload_receipt"),
        InlineKeyboardButton(text="⚙️ Настройки", callback_data="settings"),
        InlineKeyboardButton(text="Назад", callback_data="back")
    )
    builder.adjust(1)
    return builder.as_markup()

def get_back_button():
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Назад", callback_data="back")
    )
    builder.adjust(1)
    return builder.as_markup()


def get_cancel_button():
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Отмена", callback_data="cancel")
    )
    builder.adjust(1)
    return builder.as_markup()


def get_process_decision():
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Сохранить", callback_data="save_receipt"),
        InlineKeyboardButton(text="Редактировать", callback_data="edit_receipt"), #ещё не делал
        InlineKeyboardButton(text="В главное меню", callback_data="menu")
    )
    builder.adjust(2)
    return builder.as_markup()