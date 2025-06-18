from asyncio import run
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from config.token_settings import bot_token
from utils.menu import start_handler, menu_handler

async def main():
    bot = Bot(token=bot_token, default=DefaultBotProperties(parse_mode="HTML"))
    dp = Dispatcher()
    dp.message.register(start_handler, Command("start"))
    dp.message.register(menu_handler, F.text == "Menu")
    dp.message.register(menu_handler, F.text == "Back")
    await dp.start_polling(bot)

if __name__ == "__main__":
    run(main())
