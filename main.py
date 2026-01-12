#main.py

import asyncio
import logging

import config
from bot import bot
from database.connection import init_db, get_db

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from handlers.commands import router as commands_router
from handlers.callbacks import router as callbacks_router

TOKEN = config.api_key

logging.getLogger("aiogram").setLevel(logging.WARNING)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(),  # вывод в консоль
    ]
)

logger = logging.getLogger(__name__)

dp = Dispatcher()
dp.include_router(commands_router)
dp.include_router(callbacks_router)

async def main():
    try:
        await init_db()
        logger.info('✅ БД инициализирована')
    except Exception as e:
        logger.error(f'❌ Ошибка инициализации БД: {e}')
        return

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
