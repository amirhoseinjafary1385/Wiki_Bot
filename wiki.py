from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
import asyncio
from wiki import api
import wikipedia as wiki


api = ""

bot = Bot(token=api)
dp = Dispatcher()
router = Router()
wiki.set_lang('fa')

@router.message(Command('start'))
async def welcome(pm: types.Message):
    await pm.answer('Give me an Researchers...')	


@router.message()
async def wikip(pm: types.Message):
	page = wiki.page(pm.text)
	summ = wiki.summary(pm.text)
	
	result = f'''


	'''
	await pm.answer(result)

async def main():
	dp.include_router(router)
	await dp.start_polling(bot)


asyncio.run(main())
