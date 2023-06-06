from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuPython = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="#00 Python darslari"),
            KeyboardButton(text="#01 mohirdev.uz bilan tanishuv"),
            KeyboardButton(text="#02 Brauzerda kod yozish"),
            KeyboardButton(text="#03 Anaconda o'rnatamiz"),
            KeyboardButton(text="#04 Birinchi dasturimiz"),
        ],
        [
            KeyboardButton(text="Ortga"),
            KeyboardButton(text="Boshiga"),
        ],
    ],
    resize_keyboard=True
)