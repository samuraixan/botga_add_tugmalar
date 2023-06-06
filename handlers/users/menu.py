from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.default.algoKeyboard import menuAlgoritm
from keyboards.default.menuKeyboard import menu
from keyboards.default.mktbotikKeyboard import menuBotik
from keyboards.default.pythonKeyboard import menuPython

from loader import dp

@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Kurslarni tanlang", reply_markup=menu)

@dp.message_handler(text="DASTURLASH ASOSLARI")
async def send_link(message: Message):
    await message.answer("Mavzuni tanlang", reply_markup=menuPython)

@dp.message_handler(text="#00 Python darslari")
async def send_link(message: Message):
    await message.answer("https://www.youtube.com/watch?v=ZqFjXM8k-PY&list=PLwsopmzfbOn9Lw5D7a26THpBDgAma1Sus")

@dp.message_handler(text="#01 mohirdev.uz bilan tanishuv")
async def send_link(message: Message):
    await message.answer("https://www.youtube.com/watch?v=nitlLnbp7ak&list=PLwsopmzfbOn9Lw5D7a26THpBDgAma1Sus&index=2")

@dp.message_handler(text="#02 Brauzerda kod yozish")
async def send_link(message: Message):
    await message.answer("https://www.youtube.com/watch?v=fTaLQKNuOXU&list=PLwsopmzfbOn9Lw5D7a26THpBDgAma1Sus&index=3")

@dp.message_handler(text="#03 Anaconda o'rnatamiz")
async def send_link(message: Message):
    await message.answer("https://www.youtube.com/watch?v=xforSDte5-4&list=PLwsopmzfbOn9Lw5D7a26THpBDgAma1Sus&index=4")

@dp.message_handler(text="#04 Birinchi dasturimiz")
async def send_link(message: Message):
    await message.answer("https://www.youtube.com/watch?v=dguiNk8eHPY&list=PLwsopmzfbOn9Lw5D7a26THpBDgAma1Sus&index=5")

@dp.message_handler(text="MA'LUMOTLAR TUZILMASI VA ALGORITMLAR")
async def send_link(message: Message):
    await message.answer("Mavzuni tanlang", reply_markup=menuAlgoritm)

@dp.message_handler(text="#00 Kirish darsi")
async def send_link(message: Message):
    await message.answer("https://www.youtube.com/watch?v=B56tkdlfuec&list=PLwsopmzfbOn8aR9xpU7ePK30scihq4zuW")

@dp.message_handler(text="#01 Algoritm nima?")
async def send_link(message: Message):
    await message.answer("https://www.youtube.com/watch?v=KgOmr6eW5R4&list=PLwsopmzfbOn8aR9xpU7ePK30scihq4zuW&index=2")

@dp.message_handler(text="#02 Binary Search")
async def send_link(message: Message):
    await message.answer("https://www.youtube.com/watch?v=KGWsvmYVBbM&list=PLwsopmzfbOn8aR9xpU7ePK30scihq4zuW&index=3")

@dp.message_handler(text="#03 Big O")
async def send_link(message: Message):
    await message.answer("https://www.youtube.com/watch?v=MTZx5ujFTzU&list=PLwsopmzfbOn8aR9xpU7ePK30scihq4zuW&index=4")

@dp.message_handler(text="#04 Array")
async def send_link(message: Message):
    await message.answer("https://www.youtube.com/watch?v=qP0weoTLN9E&list=PLwsopmzfbOn8aR9xpU7ePK30scihq4zuW&index=5")

@dp.message_handler(text="MUKAMMAL TELEGRAM BOT")
async def send_link(message: Message):
    await message.answer("Mavzuni tanlang", reply_markup=menuBotik)

@dp.message_handler(text="#00 Kurs bilan tanishuv")
async def send_link(message: Message):
    await message.answer("https://www.youtube.com/watch?v=oRSa8NXWMXQ&list=PLwsopmzfbOn8x3CJKdQLtqDKhaF8n2r_7")

@dp.message_handler(text="#01 Kerakli dasturlar")
async def send_link(message: Message):
    await message.answer("https://www.youtube.com/watch?v=5qUTBMJLGfM&list=PLwsopmzfbOn8x3CJKdQLtqDKhaF8n2r_7&index=2")

@dp.message_handler(text="#02 Metodologiya")
async def send_link(message: Message):
    await message.answer("https://www.youtube.com/watch?v=8nsEBxH7IYA&list=PLwsopmzfbOn8x3CJKdQLtqDKhaF8n2r_7&index=3")

@dp.message_handler(text="#03 BotFather")
async def send_link(message: Message):
    await message.answer("https://www.youtube.com/watch?v=NVE9VpjUbJI&list=PLwsopmzfbOn8x3CJKdQLtqDKhaF8n2r_7&index=4")

@dp.message_handler(text="#04 aiogram")
async def send_link(message: Message):
    await message.answer("https://www.youtube.com/watch?v=FXu9Y0BN1a0&list=PLwsopmzfbOn8x3CJKdQLtqDKhaF8n2r_7&index=5")

@dp.message_handler(text="Boshiga")
async def show_menu(message: Message):
    await message.answer("Kurslarni tanlang", reply_markup=menu)

