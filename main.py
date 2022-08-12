import os
import sqlite3

import pandas as pd
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import filters
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from dotenv import load_dotenv

import markups as nav

load_dotenv()
storage = MemoryStorage()
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)
con = sqlite3.connect('db.db')
cur = con.cursor()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    msg = ('Привет! Ты можешь загрузить мне excel таблицу со списком сайтов, '
           'а я добавлю их в БД :)')
    await bot.send_message(
        message.from_user.id,
        msg,
        reply_markup=nav.file
    )


class FileInput(StatesGroup):
    file = State()


@dp.message_handler(filters.Text(equals='Загрузить файл',
                    ignore_case=True), state=None)
async def upload_xls(message: types.Message):
    if message.chat.type == 'private':
        await FileInput.file.set()
        await bot.send_message(
            message.from_user.id,
            'Отправьте мне файл xls',
            reply_markup=nav.main_menu
        )


@dp.message_handler(content_types=['document', 'text'], state=FileInput.file)
async def load_file(message: types.Message, state: FileInput):
    if message.text == 'Отмена':
        await bot.send_message(
            message.from_user.id,
            'Отменено',
            reply_markup=nav.main_menu
        )
        await state.finish()
    else:
        await message.document.download(destination_file='data/file1.xlsx')
        excel_data_df = pd.read_excel(
            'data/file1.xlsx',
            header=None,
            index_col=False
        )
        await bot.send_message(message.from_user.id, excel_data_df)
        excel_data_df.to_sql("Sites", con, if_exists="replace", index=False)
        await bot.send_message(
            message.from_user.id,
            'Данные записаны в БД успешно',
            reply_markup=nav.file
        )
        await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
