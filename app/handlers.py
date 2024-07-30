import asyncio

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, CommandObject
from aiogram.enums import ChatAction

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import app.keyboards as kb


router = Router()

class Reg(StatesGroup):
    name = State()
    number = State()
    photo = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                       action=ChatAction.TYPING)
    # await asyncio.sleep (1)
    await message.answer('Приветствуем Вас в телеграмм боте компании Юнит Групп! \nМы хотим услышать Ваш отзыв о работе компании, поделиться контактами соответствующих отделов. \nДля этого выберите один из пунктов меню! ', reply_markup=kb.main)
    # # ответ в даилоге и обычная клавиатура
    # await message.reply('Приветствуем Вас в телеграмм боте компании Юнит Групп!', reply_markup=kb.main) 
    # ответ на конкретное сообщение и  inline клавиатура

@router.callback_query(F.data == 'home')
async def cmd_contact(callback: CallbackQuery):
    await callback.answer('Контакты')
    await callback.message.answer('Вы перешли в главный раздел. \nВыберите один из пунктов.', reply_markup=kb.inline_home)

@router.callback_query(F.data == 'contact')
async def cmd_contact(callback: CallbackQuery):
    await callback.answer('Вы запросили контакты')
    await callback.message.answer('Контакты', reply_markup=kb.inline_contact)

    
@router.callback_query(F.data == 'adress') 
async def cmd_contact(callback: CallbackQuery):
    await callback.answer('Вы запросили адреса')
    await callback.message.answer('Адреса компании', reply_markup=kb.inline_adress)


@router.callback_query(F.data == 'catalog')
async def cmd_contact(callback: CallbackQuery):
    await callback.answer('Вы запросили каталог')
    await callback.message.answer('Каталог', reply_markup=kb.inline_catalog)

@router.callback_query(F.data == 'review')
async def cmd_contact(callback: CallbackQuery):
    await callback.answer('Вы запросили отзывы')
    await callback.message.answer('Отзывы', reply_markup=kb.inline_review)
    
@router.callback_query(F.data == 'predl')
async def cmd_contact(callback: CallbackQuery):
    await callback.answer('Вы запросили предложения')
    await callback.message.answer('Предложения', reply_markup=kb.inline_predl)

# ПРИМЕР ловить callback
# @router.callback_query(F.data == 'XXXXX')
# async def cmd_contact(callback: CallbackQuery):
#     await callback.answer('Вы запросили XXXXX')
#     await callback.message.answer('Контакты', reply_markup=kb.inline_XXXXX)
    


@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фотографии: {message.photo[-1].file_id}')