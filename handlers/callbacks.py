#callbacks.py

from aiogram import Router, types

from handlers.navigation_instance import nav_instance
from keyboards import builders

router = Router()

@router.callback_query(lambda c: c.data == "menu")
async def menu(call: types.CallbackQuery):
    current_text = call.message.text
    current_keyboard = call.message.reply_markup

    nav_instance.push(call.from_user.id, current_text, current_keyboard)
    await call.message.edit_text(
        text="Главное меню",
        reply_markup=builders.get_main_menu()
    )
    await call.answer()

@router.callback_query(lambda c: c.data == "stats")
async def stats(call: types.CallbackQuery):
    current_text = call.message.text
    current_keyboard = call.message.reply_markup

    nav_instance.push(call.from_user.id, current_text, current_keyboard)

    await call.message.edit_text(
        text="📊 Ваша статистика за месяц:\n- Потрачено: 10 000₽\n- Чеков: 15",
        reply_markup=builders.get_back_button()
    )
    await call.answer()

@router.callback_query(lambda c: c.data == "back")
async def back_to_menu(call: types.CallbackQuery):
    state = nav_instance.pop(call.from_user.id)
    if state:
        text, keyboard = state
        await call.message.edit_text(text=text, reply_markup=keyboard)
    await call.answer()

