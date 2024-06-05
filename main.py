import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv
from os import getenv
import logging


load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message: types.Message):
    print("Message", message)
    print("User info", message.from_user)

    name = message.from_user.first_name
    surname = message.from_user.first_name
    await message.answer(
        f"Привет, {name}" + " {surname}"
    )
    

@dp.message(Command("picture"))
async def picture_handler(message: types.Message):
    file = types.FSInputFile("images/cat.jpg")
    # await message.answer_photo(photo=file, caption="Котик")
    await message.reply_photo(photo=file, caption="Котик")

@dp.message(Command("myinfo"))
async def info_handler(message: types.Message):
    await message.answer(
        "id=745058548"
        "your first name is {name}"
        f"your name is " + "{surname}"
        

        )


@dp.message()
async def echo_handler(message: types.Message):
    await message.reply(message.text)


async def main():
    # запускаем бот
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())