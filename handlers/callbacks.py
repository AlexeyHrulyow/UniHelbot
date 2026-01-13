#callbacks.py

from aiogram import Router, types
from aiogram.fsm.context import FSMContext

from handlers.navigation_instance import nav_instance
from handlers.states import ReceiptStates
from keyboards import builders


router = Router()

@router.callback_query(lambda c: c.data == "cancel")
async def cancel(call: types.CallbackQuery, state: FSMContext):
    await state.clear()

    # Возвращаемся по навигации
    nav_state = nav_instance.pop(call.from_user.id)
    if nav_state:
        text, keyboard = nav_state
        await call.message.edit_text(text=text, reply_markup=keyboard)
    else:
        # Если нет истории, показываем главное меню
        await call.message.edit_text(
            text="Главное меню",
            reply_markup=builders.get_main_menu()
        )

    await call.answer()

@router.callback_query(lambda c: c.data == "back")
async def back_to_menu(call: types.CallbackQuery):
    state = nav_instance.pop(call.from_user.id)
    if state:
        text, keyboard = state
        await call.message.edit_text(text=text, reply_markup=keyboard)
    await call.answer()

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

@router.callback_query(lambda c: c.data == "upload_receipt")
async def upload_receipt(call: types.CallbackQuery, state: FSMContext):
    current_text = call.message.text
    current_keyboard = call.message.reply_markup

    nav_instance.push(call.from_user.id, current_text, current_keyboard)

    await call.message.edit_text(
        text = "Жду ваш чек",
        reply_markup = builders.get_cancel_button()
    )
    await state.set_state(ReceiptStates.waiting_photo)

@router.callback_query(lambda c: c.data == "save_receipt")
async def save_receipt(call: types.CallbackQuery):
    current_text = call.message.text
    current_keyboard = call.message.reply_markup

    nav_instance.push(call.from_user.id, current_text, current_keyboard)

    #Сохранение данных из чека в бд

    await call.message.edit_text(
        text="Ваш чек сохранён в базу",
        reply_markup=builders.get_main_menu()
    )
    await call.answer()
