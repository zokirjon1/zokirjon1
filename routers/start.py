from aiogram import Router, types
from aiogram.filters import CommandStart, Command

from constantas import (MAIN_TEXT, LANG_TEXT)
from keyboard.keyboard import (main_button, lang_button)
from config import init_db_pool, close_db_pool, add_user

router = Router()


@router.message(CommandStart())
async def start(message: types.Message):
    await message.answer(MAIN_TEXT, reply_markup=main_button())



@router.message(Command('lang'))
async def lang_(message: types.Message):
    await message.answer(LANG_TEXT, reply_markup=lang_button())
