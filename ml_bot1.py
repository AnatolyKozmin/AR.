from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
import asyncio

from slovar1 import startcmd_text, faq_msg
API_TOKEN = ''
#API_TOKEN = '7849617793:AAEJNOPWh8UaIA5Biru3oPC8GIbs_XA1k2I' 
# tg @sha2_assistantbot

bot = Bot(token=API_TOKEN) # создаем экземпляр бота, точка входа в программу 
dp = Dispatcher() # это нужно для того, чтобы наш бот обрабатывал наши сообщения/события 


def start_inline_kb():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="FAQ",
        callback_data="send_message"
    )
    return builder.as_markup()


@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer(startcmd_text, reply_markup=start_inline_kb())


@dp.callback_query(lambda c: c.data == "send_message")
async def handle_button(callback: types.CallbackQuery):
    await callback.message.answer(faq_msg)
    
    await callback.answer()


f'''
if __name__ == "__main__": 
     asyncio.run(dp.start_polling()) Здесь не был передан обязательный параметр экзмепляра бота, переменная bot  стр.11
     start_pooling щбязательно должен идти с await 
'''

async def main():
    print("Бот запущен!")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())