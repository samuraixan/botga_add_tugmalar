from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuBotik = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="#00 Kurs bilann tanishuv"),
            KeyboardButton(text="#01 Kerakli dasturlar"),
            KeyboardButton(text="#02 Metodologiya"),
            KeyboardButton(text="#03 BotFather"),
            KeyboardButton(text="#04 aiogram"),
        ],
        [
            KeyboardButton(text="Ortga"),
            KeyboardButton(text="Boshiga")
        ],
    ],
    resize_keyboard=True
)