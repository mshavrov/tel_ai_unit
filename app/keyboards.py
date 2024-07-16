from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup)


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Перезвоните мне', request_contact=True), KeyboardButton(text='Контакты', callback_data='my_contact' )],
    [KeyboardButton(text='Каталог компании', url='https://tdunit.ru/katalog-tovarov.html')],
    [KeyboardButton(text='Получить  скидку', url='https://tdunit.ru/ya_form-sale'), KeyboardButton(text='Заказать образец', url='https://tdunit.ru/sample')]
],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню!')

main_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Поделиться ', callback_data='my_contact'), InlineKeyboardButton(text='Адреса', url='https://ya.cpm')],
    [InlineKeyboardButton(text='Где я?', url='https://ya.cpm')]
])


# async def my_contact():
#     all 