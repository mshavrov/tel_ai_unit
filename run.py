# TOKEN='466306343:AAF_8kY66C06QiUxVdLgkw_NjOrotTD2o88'

import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

bot = Bot(token='466306343:AAF_8kY66C06QiUxVdLgkw_NjOrotTD2o88')
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
       asyncio.run(main())