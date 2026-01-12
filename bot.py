from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config import api_key

bot = Bot(token=api_key, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()