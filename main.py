from aiogram import Bot, Dispatcher, executor
from dotenv import load_dotenv
from os import getenv
import logging
from handler.mat import filter_messages
from handler.admin_ans import yes_no

logging.basicConfig(level=logging.INFO)

load_dotenv()
bot = Bot(getenv('BOT_TOKEN'))
dp = Dispatcher(bot)


dp.register_message_handler(yes_no, commands=['да'], commands_prefix=['!'])
dp.register_message_handler(filter_messages)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
