from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup)



# main contact_inline = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text='Контакты', callback_data='contact'), KeyboardButton(text='Адреса', callback_data='adress')],
#     [KeyboardButton(text='Каталог компании', callback_data='catalog')],
#     [KeyboardButton(text='Отзывы', callback_data='review'), KeyboardButton(text='Предложения', callback_data='predl')]
# ],
#                            resize_keyboard=True,
#                            input_field_placeholder='Выберите пункт меню!')

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Контакты', callback_data='contact'), InlineKeyboardButton(text='Адреса', callback_data='adress')],
    [InlineKeyboardButton(text='Каталог компании', callback_data='catalog')],
    [InlineKeyboardButton(text='Отзывы', callback_data='review'), InlineKeyboardButton(text='Предложения', callback_data='predl')]
]) 

inline_home = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Контакты', callback_data='contact'), InlineKeyboardButton(text='Адреса', callback_data='adress')],
    [InlineKeyboardButton(text='Каталог компании', callback_data='catalog')],
    [InlineKeyboardButton(text='Отзывы', callback_data='review'), InlineKeyboardButton(text='Предложения', callback_data='predl')]
]) 

inline_contact = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Оптовый отдел', callback_data='opt'), InlineKeyboardButton(text='Розничный магазин', callback_data='rozn')],
    [InlineKeyboardButton(text='Отдел закупок', callback_data='zakup'), InlineKeyboardButton(text='Предложения', callback_data='service')],
    [InlineKeyboardButton(text='Вернуться назад', callback_data='home')]
]) 

inline_adress = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Адрес магазина', callback_data='sklad_39'), InlineKeyboardButton(text='Адрес склада', callback_data='murino')],
    [InlineKeyboardButton(text='Офис компании', url='https://tel:+78126482312'), InlineKeyboardButton(text='Интернет магазин', url='https://upakovka-spb.ru/')],
    [InlineKeyboardButton(text='Вернуться назад', callback_data='home')]
    
]) 

inline_catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='УПАКОВКА', callback_data='sklad_39'), InlineKeyboardButton(text='ОДНОРАЗОВАЯ ПОСУДА', callback_data='murino')],
    [InlineKeyboardButton(text='ХОЗТОВАРЫ', callback_data='office'), InlineKeyboardButton(text='ХИМИЯ', callback_data='home')],
    [InlineKeyboardButton(text='БУМАЖНАЯ ПРОДУКЦИЯ', callback_data='sklad_39'), InlineKeyboardButton(text='ТОВАРЫ для ГОТОВКИ и СЕРВИРОВКИ', callback_data='murino')],
    [InlineKeyboardButton(text='ПОЛОТНО и ПЕРЧАТКИ', callback_data='sklad_39'), InlineKeyboardButton(text='КАНЦТОВАРЫ и КАССОВАЯ ЛЕНТА', callback_data='murino')],
    [InlineKeyboardButton(text='Вернуться назад', callback_data='home')]
]) 

inline_review = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Отзыв по заказу', callback_data='sklad_39'), InlineKeyboardButton(text='Отзыв по доставке', callback_data='sklad_39')],
    [InlineKeyboardButton(text='Вернуться назад', callback_data='home')]
])

inline_predl = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Для отдела закупок', callback_data='zakup'), InlineKeyboardButton(text='Услуги для компании', callback_data='service')],
    [InlineKeyboardButton(text='Список вызываем', callback_data='google_menu'), InlineKeyboardButton(text='Вернуться назад', callback_data='home')]
])