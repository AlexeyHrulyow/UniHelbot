#receipts.py

import os
from aiogram import Router, types, F
from aiogram.enums import ContentType
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from bot import bot
from handlers.navigation_instance import nav_instance
from handlers.states import ReceiptStates
from keyboards import builders

router = Router()

@router.message(
    F.content_type == ContentType.PHOTO,
    StateFilter(ReceiptStates.waiting_photo)
)
async def handle_receipt_photo(message: types.Message, state: FSMContext):
    if message.photo:
        photo_info = message.photo[-1]
        photo_file = await bot.get_file(photo_info.file_id)

        RECEIPT_DIR = "data/receipts"
        os.makedirs(RECEIPT_DIR, exist_ok=True)

        photo_path = os.path.join(RECEIPT_DIR, f'{message.message_id}.jpg')
        await bot.download(photo_file, destination=photo_path)
        await state.update_data(photo_path=photo_path)

        await message.answer(
            "Ваше фото сохранено, начинаю обработку",
        )
        await state.set_state(ReceiptStates.photo_processing)

        await process_receipt(message, state) #Заглушка


async def process_receipt(message: types.Message, state: FSMContext):
    """Заглушка для обработки чека"""
    # Получаем данные из состояния
    data = await state.get_data()
    photo_path = data.get('photo_path', 'неизвестно')

    # Заглушка для OCR
    receipt_data = {
        'store': 'Пятерочка',
        'total': 1234.56,
        'date': '2024-01-15',
        'items': [
            {'name': 'Молоко', 'price': 85.50, 'quantity': 1},
            {'name': 'Хлеб', 'price': 45.00, 'quantity': 1}
        ]
    }

    # Сохраняем результат в FSM
    await state.update_data(receipt_data=receipt_data)

    # Формируем текст для подтверждения
    items_text = "\n".join([f"• {item['name']} - {item['price']}₽" for item in receipt_data['items']])
    confirmation_text = (
        f"🏪 Магазин: {receipt_data['store']}\n"
        f"💰 Сумма: {receipt_data['total']}₽\n"
        f"📅 Дата: {receipt_data['date']}\n\n"
        f"🛒 Товары:\n{items_text}\n\n"
        f"Всё верно?"
    )

    # Сохраняем текущее состояние в навигацию (чтобы можно было вернуться)
    nav_instance.push(
        message.from_user.id,
        "Обработка чека",
        builders.get_cancel_button()
    )

    await message.answer(
        text=confirmation_text,
        reply_markup=builders.get_process_decision()
    )

