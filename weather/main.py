import input_from_chat
import messages
import config
from aiogram import Bot, Dispatcher, executor, types


bot = Bot(token=config.BOT_API)
Disp = Dispatcher(bot)

@Disp.message_handler(commands='help')
async def help(message: types.Message):
    await message.answer(text=f'This bot can get the current weather from your IP address.',
                         reply_markup=input_from_chat.HELP)


@Disp.message_handler(commands=['start', 'weather'])
async def show_weather(message: types.Message):
    await message.answer(text=messages.weather(), reply_markup=input_from_chat.WEATHER)


@Disp.message_handler(commands='wind')
async def show_wind(message: types.Message):
    await message.answer(text=messages.wind(), reply_markup=input_from_chat.WIND)


@Disp.message_handler(commands='sun_time')
async def show_sun_time(message: types.Message):
    await message.answer(text=messages.sun_time(), reply_markup=input_from_chat.SUN_TIME)


@Disp.callback_query_handler(text='weather')
async def callback_weather(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.weather(),
        reply_markup=input_from_chat.WEATHER
    )


@Disp.callback_query_handler(text='wind')
async def callback_wind(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.wind(),
        reply_markup=input_from_chat.WIND
    )


@Disp.callback_query_handler(text='sun_time')
async def callback_sun_time(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.sun_time(),
        reply_markup=input_from_chat.SUN_TIME
    )


if __name__ == '__main__':
    executor.start_polling(Disp)
