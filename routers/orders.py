from aiogram import Router, types, F

from config import init_db_pool, add_user, close_db_pool
from constantas import (BALANS, BALANS_TEXT, PLAY, PLAY_TEXT, FREE_TV, FREE_TV_TEXT, FREE_RADIO,
                        GAMES_BEELINE, PRESSA, PRESSA_TEXT, GAMES_BEELINE_TEXT, FREE_RADIO_TEXT, MAIN_TEXT,
                        ASOSIY_MENYU, PAKET_4G, PAKET_TEXT, PAKET_KUN, PAKET_OY, PAKET_HAFTA,
                        PAKET_HAFTA_TEXT, PAKET_OY_TEXT, PAKET_KUN_TEXT, BACK, BALANS_1, BALANS_1_TEXT,
                        TARIF_VA_XIZMATLAR, TVX_TEXT, KONTACT_TEXT, BEELINE_CLUB, CLUP_TEXT, CHEGIRMA,
                        XIZMATLAR, TARIFLAR, INTERNET_P, MENING_X, BEEGUDOK, BACK_1, BACK_2, BACK_3, MY_CLUP, INFO_UZ)
from keyboard.keyboard import (balans_button, play_button, free_tv_button, free_radio_button, oyin_button,
                               pressa_button, main_button, pakat_4g_button, asosiy, balans1_button,
                               tvx, clup_info, chegirma_button, xizmatlar_button, tariflar_button)

router = Router()


# -----------------> BALANS BOLIMI <---------------------#
@router.message(F.text == BALANS)
async def salom(message: types.Message):
    await message.reply(BALANS_TEXT, reply_markup=balans_button())


# ------------------> Kontakti beelinega tekshirish
@router.message(F.content_type.in_({'contact'}))
async def kontakt(message: types.Message):
    ans = str(message.contact.phone_number)
    await init_db_pool()
    await add_user(message.from_user.id, message.from_user.full_name, ans)
    await message.answer(text=KONTACT_TEXT, reply_markup=asosiy())
    await close_db_pool()
    # if str(message.contact.phone_number)[:] == "+998888688783":
    #     await message.reply(text=KONTACT_TEXT,  reply_markup=asosiy())
    # elif str(message.contact.phone_number)[:6] == "+99890":
    #     await message.reply(text=KONTACT_TEXT, reply_markup=asosiy())
    # else:
    #     await message.reply('Kechirasiz siz beeline foydalanuvchisi emassiz🤨')


# -------------------> PLAY BOLIMI <-----------------------#
@router.message(F.text == PLAY)
async def play_menyu(message: types.Message):
    await message.answer(text=PLAY_TEXT, reply_markup=play_button())


@router.message(F.text == FREE_TV)
async def free_tv(message: types.Message):
    await message.answer(text=FREE_TV_TEXT, reply_markup=free_tv_button())


@router.message(F.text == FREE_RADIO)
async def free_tv(message: types.Message):
    await message.answer(text=FREE_RADIO_TEXT, reply_markup=free_radio_button())


@router.message(F.text == GAMES_BEELINE)
async def free_tv(message: types.Message):
    await message.answer(text=GAMES_BEELINE_TEXT, reply_markup=oyin_button())


@router.message(F.text == PRESSA)
async def free_tv(message: types.Message):
    await message.answer(text=PRESSA_TEXT, reply_markup=pressa_button())


@router.message(F.text == ASOSIY_MENYU)
async def free_tv(message: types.Message):
    await message.answer(text=MAIN_TEXT, reply_markup=main_button())


# -----------------> 4G PAKET BOLIMI <-----------------------#

@router.message(F.text == PAKET_4G)
async def pakat_4g(message: types.Message):
    await message.answer(text=PAKET_TEXT, reply_markup=pakat_4g_button())


@router.message(F.text == PAKET_KUN)
async def pakat_4g(message: types.Message):
    await message.answer(text=PAKET_KUN_TEXT, reply_markup=pakat_4g_button())


@router.message(F.text == PAKET_OY)
async def pakat_4g(message: types.Message):
    await message.answer(text=PAKET_OY_TEXT, reply_markup=pakat_4g_button())


@router.message(F.text == PAKET_HAFTA)
async def pakat_4g(message: types.Message):
    await message.answer(text=PAKET_HAFTA_TEXT, reply_markup=pakat_4g_button())


@router.message(F.text == BACK)
async def orqaga_(message: types.Message):
    await message.answer(text="sizga kerakli bolimdi tanlim",reply_markup=main_button())


# -----------------------> ASOSIY BOLIM <-------------------------------#

@router.message(F.text == BALANS_1)
async def balans_1(msg: types.Message):
    await msg.answer(text=BALANS_1_TEXT, reply_markup=balans1_button())


@router.message(F.text == BACK_1)
async def balans_1(msg: types.Message):
    await msg.answer(text='Xizmatlardan birini tanlang:', reply_markup=asosiy())


# ------------------------> TARIF VA XIZMATLAR BOLIMI <------------------------#


@router.message(F.text == TARIF_VA_XIZMATLAR)
async def tarif_v_xizmat(msg: types.Message):
    await msg.answer(text=TVX_TEXT, reply_markup=tvx())


@router.message(F.text == BACK_2)
async def tarif_v_xizmat(msg: types.Message):
    await msg.answer(text='Xizmatlardan birini tanlang:', reply_markup=tvx())


@router.message(F.text == BACK_3)
async def tarif_v_xizmat(msg: types.Message):
    await msg.answer(text='Xizmatlardan birini tanlang:', reply_markup=asosiy())


@router.message(F.text == BEELINE_CLUB)
async def beeline_clup(msg: types.Message):
    await msg.answer(text=CLUP_TEXT, reply_markup=clup_info())


@router.message(F.text == CHEGIRMA)
async def chegirma(msg: types.Message):
    await msg.answer(text=CHEGIRMA, reply_markup=chegirma_button())


@router.message(F.text == XIZMATLAR)
async def xizmatlar(msg: types.Message):
    await msg.answer(text=XIZMATLAR, reply_markup=xizmatlar_button())


@router.message(F.text == XIZMATLAR)
async def xizmatlar(msg: types.Message):
    await msg.answer(text="Xizmatlardan birini tanlang:", reply_markup=xizmatlar_button())


@router.message(F.text == TARIFLAR)
async def tariflar(msg: types.Message):
    await msg.answer(text=TVX_TEXT, reply_markup=tariflar_button())


@router.message(F.text == INTERNET_P)
async def tariflar(msg: types.Message):
    await msg.answer(text=INTERNET_P, )


@router.message(F.text == MENING_X)
async def tariflar(msg: types.Message):
    await msg.answer(text=MENING_X, )


@router.message(F.text == BEEGUDOK)
async def tariflar(msg: types.Message):
    await msg.answer(text=BEEGUDOK, )


@router.message(F.text == MY_CLUP)
async def tariflar(msg: types.Message):
    await msg.answer(text="Mening Beeline Blub 2.0", )


@router.message(F.text == INFO_UZ)
async def tariflar(msg: types.Message):
    await msg.answer(text=INFO_TEXT, )





