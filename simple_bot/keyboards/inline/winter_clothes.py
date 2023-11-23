from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

wearing_winter = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Bosh kiyimlar👒", switch_inline_query_current_chat="bosh kiyimlar"),
        InlineKeyboardButton(text="Oyoq kiyimlar👟", switch_inline_query_current_chat="shoes")
    ],
    [
        InlineKeyboardButton(text="Shimlar👖", switch_inline_query_current_chat="shimlar"),
        InlineKeyboardButton(text="Ustki kiyimlar👕", switch_inline_query_current_chat="ustki_kiyimlar")
    ]
])


def purchasing(v: list):
    plus_button = "1"
    caption_money = int()
    if v[0] != "simple":
        l_m = str(v[1][0])
        l_m = l_m.strip(".")
        str1 = ""
        for i in l_m:
            if i != ".":
                str1 += i
        l_m = str1
        if v[0] == "plus":
            if int(l_m) == 60000 and v[1][1] == "60":
                plus_button = 2
                caption_money = 60000 * 2
            elif int(l_m) != 60000 and v[1][1] == "60":
                plus_button = (int(l_m) // 60000) + 1
                caption_money = 60000 * plus_button
        elif v[0] == "minus":
            if v[1][1] == "60" and int(l_m) == 120000:
                plus_button = 1
                caption_money = 120000 // 2
            elif v[1][1] == "60" and int(l_m) != 120000:
                plus_button = (int(l_m) // 60000) - 1
                caption_money = 60000 * plus_button
    minus = InlineKeyboardButton(text="➖", callback_data="-")
    count = InlineKeyboardButton(text=f"{str(plus_button)}", callback_data="count")
    plus = InlineKeyboardButton(text="➕", callback_data="+")
    buy = InlineKeyboardButton(text="Sotib olish", callback_data="buy")
    buying = InlineKeyboardMarkup(inline_keyboard=[
        [minus, count, plus],
        [buy]
    ])
    h_m = str(caption_money)
    if len(str(caption_money)) != 5:
        if len(str(caption_money)) == 6:
            caption_money = h_m[0] + h_m[1] + h_m[2]
            caption_money += "."
            caption_money += h_m[3] + h_m[4] + h_m[5]
        elif len(str(caption_money)) == 7:
            caption_money = h_m[0]
            caption_money += "."
            caption_money += h_m[1] + h_m[2] + h_m[3]
            caption_money += "."
            caption_money += h_m[4] + h_m[5] + h_m[6]
    elif len(str(caption_money)) == 5:
        caption_money = h_m[0] + h_m[1]
        caption_money += "."
        caption_money += h_m[2] + h_m[3] + h_m[4]
    return [buying, str(caption_money)]

