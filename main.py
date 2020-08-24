from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import aiohttp
token = '1225831912:AAG60sUGFoeRVePSufgLFM0Xaat176T2t1o'
bot = Bot(token)
dp = Dispatcher(bot)


inline_btn_1 = InlineKeyboardButton('Предложить новость', callback_data='add_news')
inline_btn_2 = InlineKeyboardButton('Вывести деньги', callback_data='get_money')
inline_btn_3 = InlineKeyboardButton('6🕕', callback_data='time6')
inline_btn_4 = InlineKeyboardButton('7🕖', callback_data='time7')
inline_btn_5 = InlineKeyboardButton('8🕗', callback_data='time8')
inline_btn_6 = InlineKeyboardButton('9🕘', callback_data='time9')
inline_btn_7 = InlineKeyboardButton('10🕙', callback_data='time10')
inline_btn_8 = InlineKeyboardButton('11🕚', callback_data='time11')
inline_btn_9 = InlineKeyboardButton('12🕛', callback_data='time12')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1, inline_btn_2)


@dp.callback_query_handler()
async def process_callback_button1(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	if callback_query.data=='add_news':
		await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text="Отправьте всю информацию которую хотите опубликовать одним сообщением")


@dp.message_handler(commands=['start', 'help'])
async def handle_start_help(message: types.Message):
	await message.answer('Привет, этот бот умеет то то и то')

@dp.message_handler(commands=['me'])
async def handle_start_help(message: types.Message):
	await message.answer('Статистика вашего аккаунта:\nопубликованные статьи:{0}\nиз них: эксклюзивов: {1}, новостей: {2}, постов: {3}\nзаработанная валюта: {4}'.format(1,2,3,4,5), reply_markup=inline_kb1)


@dp.message_handler( content_types=['document', 'audio', 'photo', 'entities', 'animation', 'video', 'video_note', 'voice'])
async def by_massage(message: types.Message):
	await message.answer(message.caption)
	await message.answer(message.document.file_id)
	

@dp.message_handler( content_types=['text'])
async def by_massage(message: types.Message):
	await message.answer(message.text)


if __name__ == '__main__':	
	executor.start_polling(dp, skip_updates=True)