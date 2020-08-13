from aiogram import Bot, Dispatcher, types, executor
import asyncio
import aiohttp
token = '1225831912:AAG60sUGFoeRVePSufgLFM0Xaat176T2t1o'
bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def handle_start_help(message: types.Message):
	await message.answer('Привет, этот бот умеет то то и то')


@dp.message_handler( content_types=['text'])
async def by_massage(message: types.Message):
	await message.answer(message.text)


if __name__ == '__main__':	
	executor.start_polling(dp, skip_updates=True)