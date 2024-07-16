import asyncio

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, CommandObject
from aiogram.enums import ChatAction

import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                       action=ChatAction.TYPING)
    # await asyncio.sleep (1)
    await message.answer('Приветствуем Вас в телеграмм боте компании Юнит Групп! ', reply_markup=kb.main)
    # # ответ в даилоге и обычная клавиатура
    # await message.reply('О джежай, приветствую тебя!!! \nМы ждали тебя!', reply_markup=kb.main) 
    # ответ на конкретное сообщение и  inline клавиатура

@router.callback_query(F.data == 'my_contact')
async def cmd_my_contact(callback: CallbackQuery):
    await callback.answer('')
    await asyncio.sleep (1)
    await callback.message.answer('Хуй')


@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фотографии: {message.photo[-1].file_id}')