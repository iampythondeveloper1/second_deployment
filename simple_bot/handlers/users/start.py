from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from keyboards.default.main_buttons import buttons
from loader import dp
from states.store import Shopping


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.delete()
    await message.answer(text=f"<i><b>Salom, {message.from_user.first_name}\n"
                         f"Ko'p vaqtingizni olmayman!\n"
                         f"Nima qiziz bo'lsa tugmalarni bosing</b></i>",
                         reply_markup=buttons)
    await Shopping.first.set()

