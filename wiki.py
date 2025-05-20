from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
import asyncio
from config import api
import wikipedia as wiki
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hbold
from aiogram.client.default import DefaultBotProperties
#from aiogram.client.session.aiohttp import AiohttpSession



bot = Bot(
	token=api,
	default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()
router = Router()
wiki.set_lang('fa')

@router.message(Command('start'))
async def welcome(pm: types.Message):
    await pm.answer('Give me an Researchers...')	


@router.message()
async def wikip(pm: types.Message):
	try:

		#page = wiki.page(pm.text)
		summary = wiki.summary(pm.text)
		
		result = f'''
		<b>🦋📚 {page.text}</b>

		🕸🕸🕸
		{summary[:3000]}
		🕸🕸🕸

		'''
		await pm.answer(result)

	except wiki.exceptions.DisambiguationError as e:
		options = "\n".join(e.options[:10]) #show first 10 options
		await pm.answer(f"Multiple options found. Please be more specific:\n\n{options}")
	except wiki.exceptions.PageError:
		await pm.answer("🔍Page not found. Please try another topic.")
	except Exception as e:
		await pm.answer(f"An error occured: {str(e)}")


async def main():
	dp.include_router(router)
	await dp.start_polling(bot)

if __name__ == "__main__":
	asyncio.run(main())
