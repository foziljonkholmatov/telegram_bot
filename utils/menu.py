from aiogram import types

from utils.keyboard_settings import user_menu, user_main


async def start_handler(message: types.Message):
    text = f"Hello, " f"{message.from_user.mention_html(f'P{message.from_user.full_name}')}"
    await message.answer(text=text, reply_markup=user_main)


async def menu_handler(message: types.Message):
    if message.text == "Back":
        await message.answer('Back to main menu', reply_markup=user_main)
    else:
        await message.answer('Menu entered', reply_markup=user_menu)
