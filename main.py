import aiogram 
import random 
import asyncio 
import logging 
from aiogram import Bot, Dispatcher, types 
from aiogram.filters.command import Command,CommandObject 
from aiogram.fsm.context import FSMContext 

from states import CalcStates 

logging.basicConfig(level=logging.INFO) 
bot = Bot(token="7128878398:AAHgFGRvfwsMlU05CZVn2JGZ8XwsPBoiG34")  
dp = Dispatcher() 

@dp.message(Command("start")) 
async def cmd_start(message: types.Message): 
    await message.answer("hello") 

@dp.message(Command("roll")) 
async def roll(message: types.Message, command: CommandObject): 
    args = [int(i) for i in command.args.split()] 
    if len(args)==2: 
        await message.answer(f'ControledRoll({random.randint(args[0], args[1])})') 
    elif len(args)==1: 
        args = [int(i)for i in command.args.split()] 
        await message.answer(f'ControledRoll({random.randint(0, args[0])})') 
    elif len(args)>= 3: 
        await message.answer(f'Вы ввели:{message.text}  \nСлучайное число из:>>>{random.choice(args)}<<<') 
    else: 
        await message.answer(f'Твое случайное число ---->{random.randint(1,100)}') 

async def main(): 
    await dp.start_polling(bot) 

if name == "__main__": 
    asyncio.run(main())