import aiogram.types
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from keyboards.default.main_buttons import buttons
from keyboards.default.main_buttons import types_of_clothes
from loader import dp
from states.store import Shopping


@dp.message_handler(text="Kiyimlar", state=Shopping.first)
async def clothes(message: types.Message, state: FSMContext):
    first_photos_file_id = ("https://avatars.mds.yandex.net/i?id="
                            "76711f6f2d208026a4664da1274a1fd0b4edd"
                            "6d9-9290563-images-thumbs&n=13")
    second_photos_file_id = ("https://avatars.mds.yandex.net/"
                             "i?id=44854d70c217ffffdd7aac0a290"
                             "5273f0b1ccf52-10069096-images-thumbs&n=13")
    third_photos_file_id = ("https://avatars.mds.yandex.net/i?id=d12b0fbc45"
                            "7873da85f052222fa3cc2f9acef8ce-10455853-images-thumbs&n=13")
    photos_album = types.MediaGroup()
    photos_album.attach_photo(photo=first_photos_file_id)
    photos_album.attach_photo(photo=second_photos_file_id)
    photos_album.attach_photo(photo=third_photos_file_id)
    await message.reply_media_group(media=photos_album)
    await message.answer(text="<em><b>Birini tanlang</b></em>",
                         reply_markup=types_of_clothes)
    await Shopping.second.set()


@dp.message_handler(text="Ro'zg'or buyumlari", state=Shopping.first)
async def special_tools(message: types.Message, state: FSMContext):
    pass


@dp.message_handler(text="Kompyuter jixozlari", state=Shopping.first)
async def comp_items(message: types.Message, state: FSMContext):
    pass


@dp.message_handler(text="Kitoblar", state=Shopping.first)
async def books(message: types.Message, state: FSMContext):
    pass

