from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

buttons = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton(text="Kiyimlar"),
        KeyboardButton(text="Ro'zg'or buyumlari")
    ],
    [
        KeyboardButton(text="Kompyuter jixozlari"),
        KeyboardButton(text="Kitoblar")
    ]
])

types_of_clothes = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Yozgi kiyimlar⛱"),
        KeyboardButton(text="Qishki kiyimlar❄️")
    ]
], resize_keyboard=True)

back_button = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton(text="Ortga⬅️")
    ]
])

