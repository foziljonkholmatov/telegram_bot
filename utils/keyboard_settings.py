from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Menu')],
        [KeyboardButton(text="My orders")],
        [
            KeyboardButton(text="Basket"),
            KeyboardButton(text="Contact")
        ],
        [
            KeyboardButton(text="Send message"),
            KeyboardButton(text="Settings")
        ],
        [KeyboardButton(text="About us")]
    ],
    resize_keyboard=True,
    is_persistent=True
)
user_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Drinks")
        ],
        [
            KeyboardButton(text="Hot-dog"),
            KeyboardButton(text="Burger")
        ],
        [   KeyboardButton(text="Back")
         ]
    ],
    resize_keyboard=True,
    is_persistent=True
)
