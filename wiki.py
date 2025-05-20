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

user_language = []	# Dictionary to store user language preferences

print("Bot Started")
dp = Dispatcher()
router = Router()

@router.message(Command('start'))
async def welcome(pm: types.Message):
	user_id = pm.from_user.id
	user_language[user_id] = 'fa'
	wiki.set_lang('fa')

	await pm.answer('''
	<b>Welcome to wikipedia Bot!</b>
	I can search wikipedia in persian or English language...

	Commands:
	/persian - Switch to Persian Wikipedia
	/english - Switch to English Wikipedia
	''')
	if user.username:
		await pm.answer(f"Hello @{user.username}! Give me a topic to search for.")
	else:
		await pm.answer(f"Hello {user.full_name}! Give me a topic to search for.")


@router.message(Command('english'))
async def set_english(pm: types.Message):
	user_id = pm.from_user.id
	user.languages[user_id] = 'en'
	await pm.answer('Search language changed to <b>English</b>.')

@router.message()
async def wikip(pm: types.Message):
	try:

		page = wiki.page(pm.text)
		summary = wiki.summary(pm.text)
		
		result = f'''
		<b>🦋📚 {page.title}</b>

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
