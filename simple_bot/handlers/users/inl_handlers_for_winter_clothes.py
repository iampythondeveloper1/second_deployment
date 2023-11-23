from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from data.products import REGULAR_SHIPPING, FAST_SHIPPING, PICKUP_SHIPPING
from keyboards.default.main_buttons import back_button
from keyboards.inline.winter_clothes import wearing_winter, purchasing
from loader import dp
from states.store import Shopping
from aiogram.types import ReplyKeyboardRemove, LabeledPrice

from utils.misc.product import Product


@dp.inline_handler(text="bosh kiyimlar", state="*")
async def hats_hand(inline: types.InlineQuery):
    await inline.answer(
        results=[
            types.InlineQueryResultArticle(
                id="1st",
                title="Qalpoq",
                input_message_content=types.InputTextMessageContent(
                    message_text="qalpoq"
                ),
                thumb_url="https://i.postimg.cc/hGHR3v9X/shaokaca.webp",
                description="60.000 so'm"
            )
        ]
    )


@dp.message_handler(text="qalpoq", state=Shopping.third)
async def hat_1(message: types.Message):
    await message.delete()
    await message.answer_photo(photo="https://i.postimg.cc/DZXn2L2Q/shaokaca.webp",
                               caption="<i><b>Oq bobonchikli, kul rang\nVa qor "
                                       "parchalar bilan qoplangan shapka👒\n\n"
                                       "Narxi🤑:</b> <code>60.000 so'm</code></i>",
                               reply_markup=purchasing(v=["simple"])[0])
    await Shopping.fourth.set()


@dp.callback_query_handler(text="+", state="*")
async def plus_one(callback: types.CallbackQuery):
    if callback.message.reply_markup.inline_keyboard[0][1]["text"] == "50":
        await callback.answer("Maximum 50ta harid qila olasiz!", show_alert=True)
        return ""
    await callback.answer()
    caption = str()
    r_c = callback.message.caption
    for i in range(len(r_c)):
        if r_c[i] == "🤑" and r_c[i + 1] == ":":
            caption += r_c[i]
            break
        else:
            caption += r_c[i]
    money = r_c.strip(caption)
    money = money.strip(":. so'm")
    if caption == ("Oq bobonchikli, kul rang\n"
                   "Va qor parchalar bilan qoplangan shapka👒\n\n"
                   "Narxi🤑") and money == "60.000":
        money = 60000
    list1 = purchasing(v=["plus", [str(money), "60"]])
    await callback.message.edit_media(media=types.InputMedia(
        types="photo",
        media="https://i.postimg.cc/DZXn2L2Q/shaokaca.webp",
        caption="<i><b>Oq bobonchikli, kul rang\nVa qor "
                "parchalar bilan qoplangan shapka👒\n\n"
                f"Narxi🤑:</b> <code>{list1[1]} so'm</code></i>"
    ), reply_markup=list1[0])


@dp.callback_query_handler(text="-", state="*")
async def minus_one(callback: types.CallbackQuery):
    if callback.message.reply_markup.inline_keyboard[0][1]["text"] == "1":
        await callback.answer(text="Minimum 1ta xarid qiling!", show_alert=False)
        return ""
    await callback.answer()
    caption = str()
    r_c = callback.message.caption
    for i in range(len(r_c)):
        if r_c[i] == "🤑" and r_c[i + 1] == ":":
            caption += r_c[i]
            break
        else:
            caption += r_c[i]
    money = r_c.strip(caption)
    money = money.strip(":. so'm")
    if caption == ("Oq bobonchikli, kul rang\n"
                   "Va qor parchalar bilan qoplangan shapka👒\n\n"
                   "Narxi🤑") and money == "120.000":
        money = 120000
    list1 = purchasing(v=["minus", [str(money), "60"]])
    await callback.message.edit_media(media=types.InputMedia(
        types="photo",
        media="https://i.postimg.cc/DZXn2L2Q/shaokaca.webp",
        caption="<i><b>Oq bobonchikli, kul rang\nVa qor "
                "parchalar bilan qoplangan shapka👒\n\n"
                f"Narxi🤑:</b> <code>{list1[1]} so'm</code></i>"
    ), reply_markup=list1[0])


@dp.callback_query_handler(text="count", state="*")
async def click_on_count(call: types.CallbackQuery):
    await call.answer()


@dp.callback_query_handler(text="buy", state="*")
async def b_b(call: types.CallbackQuery):
    r_c = call.message.caption
    caption = str()
    for i in range(len(r_c)):
        if r_c[i] == "🤑" and r_c[i + 1] == ":":
            caption += r_c[i]
            break
        else:
            caption += r_c[i]
    money = r_c.strip(caption)
    money = money.strip(":. so'm")
    money1 = ""
    for i in money:
        if i != ".":
            money1 += i
    # if len(str(money1)) in [5, 6, 7]:
    #     money1 += "00"
    white_hat = Product(
        title="Oq bobonchikli va qor "
              "parchalar bilan qoplangan qalpoq👒",
        description="To'lov qilish uchun quyidagi tugmani bosing💳",
        currency="USD",
        prices=[
            LabeledPrice(
                label="Oq Shapka",
                amount=int(money1),
            )
        ],
        start_parameter="create_invoice_beautiful_hat",
        photo_url="https://avatars.mds.yandex.net/i?id=c73a"
                  "cb7cf43eb78ac321bd448242e524e20cfbf5-10547508-images-thumbs&n=13",
        photo_width=923,
        photo_height=1290,
        photo_size=1000,
        need_name=True,
        need_email=True,
        need_phone_number=True,
        need_shipping_address=True,
        is_flexible=True
    )
    await call.message.delete()
    await dp.bot.send_invoice(chat_id=call.from_user.id,
                              **white_hat.generate_invoice(),
                              payload="payload:white_hat")
    await call.message.answer(text="💳To'lov💸",
                              reply_markup=back_button)
    await Shopping.fifth.set()


@dp.message_handler(text="Ortga⬅️", state=Shopping.fifth)
async def back_from_payment(message: types.Message):
    await message.answer(text="Qishki kiyimlar👕👚",
                         reply_markup=ReplyKeyboardRemove())
    await message.answer(text="<b>Qidirayotganingiz ustiga bosing</b>",
                         reply_markup=wearing_winter)
    await Shopping.third.set()


@dp.shipping_query_handler(state=Shopping.fifth)
async def choose_shipping(query: types.ShippingQuery):
    if query.shipping_address.country_code != "UZ":
        await dp.bot.answer_shipping_query(shipping_query_id=query.id,
                                           ok=False,
                                           error_message="Buyurtma faqat O'zbekiston hududi uchun!")
    elif query.shipping_address.city.lower() != "tashkent":
        await dp.bot.answer_shipping_query(shipping_query_id=query.id,
                                           shipping_options=[FAST_SHIPPING, REGULAR_SHIPPING, PICKUP_SHIPPING],
                                           ok=True)
    else:
        await dp.bot.answer_shipping_query(shipping_query_id=query.id,
                                           shipping_options=[FAST_SHIPPING, REGULAR_SHIPPING, PICKUP_SHIPPING],
                                           ok=True)


@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await dp.bot.answer_pre_checkout_query(pre_checkout_query_id=pre_checkout_query.id,
                                           ok=True)
    await dp.bot.send_message(chat_id=pre_checkout_query.from_user.id,
                              text="Xaridingiz uchun rahmat!")
    await dp.bot.send_message(chat_id=ADMINS[0],
                              text=f"<i>Quyidagi mahsulot sotildi✅: <b>{pre_checkout_query.invoice_payload}</b>\n"
                                   f"ID🔢: <b>{pre_checkout_query.id}</b>\n"
                                   f"Telegram user: <b>{pre_checkout_query.from_user.first_name}</b>\n"
                                   f"Xaridor: <b>{pre_checkout_query.order_info}</b>\n"
                                   f"Mobile: <b>{pre_checkout_query.order_info.phone_number}</b></i>")


