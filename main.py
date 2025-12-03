import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.enums import ParseMode

API_TOKEN = '8473817462:AAEFLo1jkrv77WliQoy4Awuiy8JHBo1lpbo'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Привет! Я бот, который всегда отвечает 'привет' на твои сообщения!")

@dp.message()
async def echo_all(message: Message):
    await message.answer("привет")

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
