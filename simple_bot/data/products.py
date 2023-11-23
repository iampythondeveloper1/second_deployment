import aiogram.types

from utils.misc.product import Product
from aiogram.types import LabeledPrice


REGULAR_SHIPPING = aiogram.types.ShippingOption(
    id="post_reg",
    title="Fargo (3 kun)",
    prices=[
        LabeledPrice(label="Maxsus quti",
                     amount=100000),
        LabeledPrice(label="2 kun ichida yetkazish",
                     amount=100000)
    ]
)

FAST_SHIPPING = aiogram.types.ShippingOption(
    id="post_fast",
    title="Express pochta (1 kun)",
    prices=[
        LabeledPrice(label="1 kunda yetkazish",
                     amount=100000)
    ]
)


PICKUP_SHIPPING = aiogram.types.ShippingOption(
    id="pickup",
    title="Do'kondan olib ketish",
    prices=[
        LabeledPrice(label="Yetkazib berishiz",
                     amount=-10000)
    ]
)

