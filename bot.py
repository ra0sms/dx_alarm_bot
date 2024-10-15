#!venv/bin/python3

import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import random
from config_reader import config

# Включаем логирование
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.bot_token.get_secret_value())
# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Hello {message.from_user.full_name}!")

# Хэндлер на команду /rand
@dp.message(Command("rand"))
async def cmd_test1(message: types.Message):
    await message.answer(f"Случайное число: {random.randint(0,100)}")

# Хэндлер на команду /test2
async def cmd_test2(message: types.Message):
    await message.reply("Test 2")


#----------------Main---------------------------- 
async def main():
    dp.message.register(cmd_test2, Command("test2"))
    dp.message.register(cmd_test1, Command("rand"))
    dp.message.register(cmd_start, Command("start"))
    await bot.send_message(591915735,text="Перезапуск")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
