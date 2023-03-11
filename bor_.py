from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from config import bot_TOKEN

bot = Bot(token=bot_TOKEN)
dp = Dispatcher(bot)

