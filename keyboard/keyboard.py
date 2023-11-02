from aiogram.utils.keyboard import KeyboardBuilder, KeyboardButton, InlineKeyboardButton
from aiogram.types import WebAppInfo

from constantas import (BALANS, PAKET_4G, PLAY, LANG_RU, LANG_UZ, KONTACT, BACK, FREE_TV, FREE_RADIO,
                                     GAMES_BEELINE, PRESSA, ASOSIY_MENYU, PAKET_KUN, PAKET_HAFTA, PAKET_OY, BALANS_1,
                                     TARIF_VA_XIZMATLAR, BEELINE_CLUB, CHEGIRMA, XIZMATLAR, TARIFLAR, INTERNET_P,
                                     MENING_X, BEEGUDOK, MY_CLUP, ALMASHTIRISH, MAVJUD_KARTALAR, INFO_UZ, HAR_DOIM,
                                     FURSATDAN, SIZ_UCHUN, SIZNING_QOLINGIZDA, KUTIB_OLING, MAXSUS, ISHONCHLI_TOLOV,
                                     MOBIL_ALOQA_INTERNET, INTERNET, XALQARO_SMS, MAXSUS_TAKLIFLAR, SMS_XABARLAR,
                                     YANA_4, YANA_3, YANA_2, YANA_1, STATUS_SILVER_2022, STATUS_GOLD_2022,
                                     STATUS_PLATINUM, STATUS_SILVER, STATUS_GOLD, ZOR_4, ZOR_1, ZOR_2, ZOR_3, OSON_10,
                                     OSON_1, KUNLIK, BACK_2, BACK_3, BACK_1)


# -------------------> MENYU <----------------------#
def main_button():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[
            KeyboardButton(text=BALANS),
            KeyboardButton(text=PAKET_4G),
            KeyboardButton(text=PLAY),
        ]
    )
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)


# -------------------> TIL TANLASH <----------------------#
def lang_button():
    builder = KeyboardBuilder(InlineKeyboardButton)

    builder.add(
        *[
            InlineKeyboardButton(text=LANG_RU, callback_data='ru'),
            InlineKeyboardButton(text=LANG_UZ, callback_data='uz'),
        ]
    )
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)


# -------------------> BALANS BOLIMI <----------------------#
def balans_button():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[
            KeyboardButton(text=KONTACT, request_contact=True),
            KeyboardButton(text=BACK)
        ]
    )
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)


# -------------------> PLAY BOLIMI <----------------------#

def play_button():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[
            KeyboardButton(text=FREE_TV),
            KeyboardButton(text=FREE_RADIO),
            KeyboardButton(text=GAMES_BEELINE),
            KeyboardButton(text=PRESSA),
            KeyboardButton(text=ASOSIY_MENYU),
        ]
    )
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)


def free_tv_button():
    builder = KeyboardBuilder(InlineKeyboardButton)
    builder.add(
        *[
            InlineKeyboardButton(text="Ko'rish ▶️", web_app=WebAppInfo(url='https://beeline.uz/uz/products/services/beeline-tv'))
        ]
    )
    return builder.as_markup(resize_keyboard=True)


def free_radio_button():
    builder = KeyboardBuilder(InlineKeyboardButton)
    builder.add(
        *[
            InlineKeyboardButton(text="Tinglash ▶️", web_app=WebAppInfo(url='https://beeline.uz/uz/products/services/beeline-music-radio'))
        ]
    )
    return builder.as_markup(resize_keyboard=True)


def oyin_button():
    builder = KeyboardBuilder(InlineKeyboardButton)
    builder.add(
        *[
            InlineKeyboardButton(text="O'ynash ▶️", web_app=WebAppInfo(url='https://beeline.uz/uz/products/services/beeline-app'))
        ]
    )
    return builder.as_markup(resize_keyboard=True)


def pressa_button():
    builder = KeyboardBuilder(InlineKeyboardButton)
    builder.add(
        *[
            InlineKeyboardButton(text="O'qish ▶️", web_app=WebAppInfo(url='https://beeline.uz/uz/products/services/beeline-pressa'))
        ]
    )
    return builder.as_markup(resize_keyboard=True)


def asosiy_menyu_button():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[
            KeyboardButton(text=ASOSIY_MENYU)
        ]
    )
    return builder.as_markup(resize_keyboard=True)


def pakat_4g_button():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[
            KeyboardButton(text=PAKET_KUN),
            KeyboardButton(text=PAKET_HAFTA),
            KeyboardButton(text=PAKET_OY),
            KeyboardButton(text=ASOSIY_MENYU),
        ]
    )
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)


def back_():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[
            KeyboardButton(text=BACK)
        ]
    )
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)


def asosiy():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[
            KeyboardButton(text=BALANS_1),
            KeyboardButton(text=TARIF_VA_XIZMATLAR),
            KeyboardButton(text=BEELINE_CLUB),
            KeyboardButton(text=CHEGIRMA),
            KeyboardButton(text=ASOSIY_MENYU)
        ]
    )
    builder.adjust(1, 1, 1, 1, 2)
    return builder.as_markup(resize_keyboard=True)


def balans1_button():
    builder = KeyboardBuilder(InlineKeyboardButton)

    builder.add(
        *[
            InlineKeyboardButton(text='Tafsilotni oching', web_app=WebAppInfo(url='https://beeline.uz/uz/Account/Login'))
        ]
    )
    return builder.as_markup(resize_keyboard=True)


def tvx():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[
            KeyboardButton(text=XIZMATLAR),
            KeyboardButton(text=TARIFLAR),
            KeyboardButton(text=INTERNET_P),
            KeyboardButton(text=MENING_X),
            KeyboardButton(text=BEEGUDOK),
            KeyboardButton(text=ASOSIY_MENYU),
            KeyboardButton(text=BACK_1)
        ]
    )
    builder.adjust(1, 1, 1, 1, 1, 2)
    return builder.as_markup(resize_keyboard=True)


def clup_info():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[
            KeyboardButton(text=MY_CLUP,web_app=WebAppInfo(url="https://beeline.uz/uz/beeline-club-new") ),
            KeyboardButton(text=ALMASHTIRISH),
            KeyboardButton(text=MAVJUD_KARTALAR),
            KeyboardButton(text=INFO_UZ),
            KeyboardButton(text=BACK_3),
            KeyboardButton(text=ASOSIY_MENYU)
        ]
    )
    builder.adjust(1, 1, 1, 1, 2)
    return builder.as_markup(resize_keyboard=True)


def chegirma_button():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[
            KeyboardButton(text=HAR_DOIM),
            KeyboardButton(text=FURSATDAN),
            KeyboardButton(text=SIZ_UCHUN),
            KeyboardButton(text=SIZNING_QOLINGIZDA),
            KeyboardButton(text=KUTIB_OLING),
            KeyboardButton(text=MAXSUS),
            KeyboardButton(text=BACK),
            KeyboardButton(text=ASOSIY_MENYU),
        ]
    )
    builder.adjust(1, 1, 1, 1, 1, 1, 2)
    return builder.as_markup(resize_keyboard=True)


def xizmatlar_button():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[
            KeyboardButton(text=ISHONCHLI_TOLOV),
            KeyboardButton(text=MOBIL_ALOQA_INTERNET),
            KeyboardButton(text=INTERNET),
            KeyboardButton(text=XALQARO_SMS),
            KeyboardButton(text=MAXSUS_TAKLIFLAR),
            KeyboardButton(text=SMS_XABARLAR),
            KeyboardButton(text=BACK_2),
            KeyboardButton(text=ASOSIY_MENYU),
        ]
    )
    builder.adjust(1, 1, 1, 1, 1, 1, 2)
    return builder.as_markup(resize_keyboard=True)
def tariflar_button():
    builder = KeyboardBuilder(KeyboardButton)
    builder.add(
        *[
            KeyboardButton(text=YANA_4),
            KeyboardButton(text=YANA_3),
            KeyboardButton(text=YANA_2),
            KeyboardButton(text=YANA_1),
            KeyboardButton(text=STATUS_SILVER_2022),
            KeyboardButton(text=STATUS_GOLD_2022),
            KeyboardButton(text=STATUS_PLATINUM),
            KeyboardButton(text=STATUS_SILVER),
            KeyboardButton(text=STATUS_GOLD),
            KeyboardButton(text=ZOR_4),
            KeyboardButton(text=ZOR_3),
            KeyboardButton(text=ZOR_2),
            KeyboardButton(text=ZOR_1),
            KeyboardButton(text=OSON_10),
            KeyboardButton(text=OSON_1),
            KeyboardButton(text=KUNLIK),
            KeyboardButton(text=ASOSIY_MENYU),
            KeyboardButton(text=BACK),
        ]
    )
    builder.adjust(2,2,1,1,1,2,2,2,2,1,2)
    return builder.as_markup(resize_keyboard=True)