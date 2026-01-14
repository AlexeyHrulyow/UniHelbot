#commands.py

from aiogram import Router, types
from aiogram.filters import Command, StateFilter
from handlers.navigation_instance import nav_instance
from handlers.states import ReceiptStates
from keyboards import builders

router = Router()


@router.message(Command("start"))
async def start(message: types.Message):
    start_text = ("Привет! Я тупорылая заглушка для проверки работы."
                  "\nСейчас я выведу главное меню.")
    keyboard = builders.get_start_menu()
    nav_instance.clear(message.from_user.id)
    await message.answer(text=start_text, reply_markup=keyboard)

@router.message(Command("menu"))
async def menu(message: types.Message):
    menu_text = "Главное меню"
    keyboard = builders.get_main_menu()

    await message.answer(menu_text, reply_markup=keyboard)
    nav_instance.push(message.from_user.id, menu_text, keyboard)

@router.message(~StateFilter(ReceiptStates.waiting_photo, ReceiptStates.photo_processing))
async def echo_handler(message: types.Message):
    await message.answer(f"Услышал тебя, дорогой: {message.text}")
