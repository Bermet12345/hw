from aiogram import types
from config import bot, dp
from aiogram.utils import executor
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton


@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await bot.send_message(message.chat.id, f'Здравствуйте, я бот к вашим услугам')


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    murkup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton('NEXT', callback_data='button1')
    murkup.add(button1)
    question = 'Кто создал Python?'
    answer = ['Гвидо ван Россум', 'Великий учёный', 'Франкенштейн']

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation= 'Ну точно же не Франкенштейн',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=murkup
    )


@dp.callback_query_handler(lambda call: call.data == 'button1')
async def quiz_2(call: types.callback_query):
    question = 'В каком году появился язык программирорвания Python?'
    answer = ['1990 году', '1999 году', '1991 году', '1993 году']

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='Инет в помощь',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
    )


@dp.message_handler(commands=['quiz1'])
async def quiz_3(message: types.Message):
    question = 'Зачем нужны языки?'
    answer = ['просто', 'для забавы', 'общения', 'учились']

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation='А для чего еще?',
        explanation_parse_mode=ParseMode.MARKDOWN_V2
    )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)