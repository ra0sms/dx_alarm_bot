#!venv/bin/python3

import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandObject
from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram.enums import ParseMode
import random
import subprocess
from config_reader import config

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()


@dp.message(Command("get"))
async def cmd_get(
        message: types.Message,
        command: CommandObject
):
    spots = ""
    if command.args is None:
        await message.answer("Ошибка: не переданы аргументы")
        return
    try:
        callsign = command.args
    except ValueError:
        await message.answer(
            "Ошибка: неправильный формат команды. Пример:\n"
            "/get <callsign>"
        )
        return
    spots = read_last_spots(callsign)
    await message.answer(
        f"DX: {callsign.upper()}\n"
        "Последние споты: \n"
        f"{spots}"
    )




@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        f"Привет {message.from_user.full_name}\n"
        "Споты за последние 15 минут:"
        " ```\n"
        "/get <позывной>\n"
        "```"
        "Например, /get ra0sms", 
        parse_mode=ParseMode.MARKDOWN_V2 
    )


@dp.message(Command("rand"))
async def cmd_rand(message: types.Message):
    await message.answer(f"Случайное число: {random.randint(0,100)}")



def read_last_spots(callsign: str) -> str:
    try:
        subprocess.run(["parse/get_spots.sh"] + [callsign])
        slash_call = callsign.replace('/', '_')
        file_path = f'parse/dx_spots/{slash_call}.txt'
        file_path_adif = f'parse/dx_spots/{slash_call}.adif'
    except Exception as e:
        return "Нет файла с dx-позывным"
    out =""

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        out += (line)
    subprocess.run(["rm"] + [file_path])
    subprocess.run(["rm"] + [file_path_adif])
    if out:
        return out
    else:
        return "Нет спотов"


#----------------Main---------------------------- 
async def main():
    dp.message.register(cmd_rand, Command("rand"))
    dp.message.register(cmd_start, Command("start"))
    dp.message.register(cmd_get, Command("get"))
    await bot.send_message(591915735,text="Перезапуск")
    await bot.set_my_commands([BotCommand(command='start', description='Начало работы')],  BotCommandScopeDefault())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

