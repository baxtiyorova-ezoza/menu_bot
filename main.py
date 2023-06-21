import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = '6295260839:AAHcvNHH48Ha2oTz_9x-SWoZhpvm1T9NUpE'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


main_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ichimliklar"),
            KeyboardButton(text="Lavashlar"),
        ], 
        [
            KeyboardButton(text="orqaga"),
        ]
    ],
    resize_keyboard=True
)

ichimlik_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Fanta"),
            KeyboardButton(text="Cola"),
        ], 
        [
            KeyboardButton(text="Pepsi"),
        ],
        [
            KeyboardButton(text="orqaga"),
        ]
    ],
    resize_keyboard=True
)


Lavash_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
     [
         KeyboardButton(text="Go'shtli Lavash"),
         KeyboardButton(text="Tovuqli Lavash"),
         KeyboardButton(text="orqaga"),
     ]
    ],
    resize_keyboard=True
    )


@dp.message_handler(commands=['start', 'menu'])
async def send_welcome(message: types.Message):
    await message.reply("Salom bu f00t_bot menu ni tanlang.", reply_markup=main_menu_keyboard)


@dp.message_handler(commands=['menu'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply(" Hot dog, Lavash...")

@dp.message_handler( text = "Ichimliklar")
async def echo(message: types.Message):
    await message.answer_photo("https://telegra.ph/file/9c230229c0651c0121359.jpg") 
    await message.answer_photo("https://zamin.uz/uploads/posts/2018-07/1531372017_28142.jpg", caption="ichimliklarni tanlang")  
    await message.answer("Mana ichimliklar", reply_markup=ichimlik_menu_keyboard)


@dp.message_handler( text = "orqaga")
async def echo(message: types.Message):
    await message.answer("Bosh menu", reply_markup=main_menu_keyboard)


@dp.message_handler( text = "Hot dog")
async def echo(message: types.Message):
    await message.answer("Hot dog 25000",)


@dp.message_handler( text = "Lavashlar")
async def echo(message: types.Message):
    await message.answer_photo("https://apps.bringo.uz/public/assets/products/250x250/1030276_546311823.jpg")
    await message.answer("Mana lavashlar",reply_markup=Lavash_menu_keyboard)
    await message.answer()


@dp.message_handler( text = "Ichimliklar")
async def echo(message: types.Message):
    await message.answer_photo("https://telegra.ph/file/9c230229c0651c0121359.jpg") 
    await message.answer_photo("https://t.me/main_pytho/2")
    await message.answer_photo("https://zamin.uz/uploads/posts/2018-07/1531372017_28142.jpg", caption="ichimliklarni tanlan")  
    await message.answer()


@dp.message_handler( text = "Fanta")
async def echo(message: types.Message):
    await message.answer("0.5 - 7 000  1.0 - 11 000  1.5 - 13 000  Fanta Cola Pepsi hammasini narxi bir xil")


@dp.message_handler( text = "pepsi")
async def echo(message: types.Message):
    await message.answer("0.5 - 7 000  1.0 - 11 000  1.5 - 13 000")


@dp.message_handler( text = "cola")
async def echo(message: types.Message):
    await message.answer("0.5 - 7 000  1.0 - 11 000  1.5 - 13 000")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("Buyurtma qabul qilindi, iltimos manzilni kiriting 📍")


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)