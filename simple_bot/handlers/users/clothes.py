from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline.winter_clothes import wearing_winter
from loader import dp
from states.store import Shopping
from aiogram.types import ReplyKeyboardRemove


@dp.message_handler(text="Qishki kiyimlar❄️", state=Shopping.second)
async def winter_clothes(message: types.Message, state: FSMContext):
    await message.answer(text="Qishki kiyimlar👕👚",
                         reply_markup=ReplyKeyboardRemove())
    await message.answer(text="<b>Qidirayotganingiz ustiga bosing</b>",
                         reply_markup=wearing_winter)
    await Shopping.third.set()


@dp.message_handler(text="Yozgi kiyimlar⛱", state=Shopping.second)
async def summer_clothes(message: types.Message, state: FSMContext):
    pass


