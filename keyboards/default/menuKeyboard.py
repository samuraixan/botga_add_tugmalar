from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="DASTURLASH ASOSLARI"),
            KeyboardButton(text="MUKAMMAL TELEGRAM BOT"),
            KeyboardButton(text="MA'LUMOTLAR TUZILMASI VA ALGORITMLAR")
        ],
    ],
    resize_keyboard=False
)