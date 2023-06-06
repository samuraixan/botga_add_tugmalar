from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuAlgoritm = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="#00 Kirish darsi"),
            KeyboardButton(text="#01 Algoritm nima?"),
            KeyboardButton(text="#02 Binary Search"),
            KeyboardButton(text="#03 Big O"),
            KeyboardButton(text="#04 Array")
        ],
        [
            KeyboardButton(text="Ortga"),
            KeyboardButton(text="Boshiga")
        ],
    ],
    resize_keyboard=True
)