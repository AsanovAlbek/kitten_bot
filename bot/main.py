from telebot import TeleBot, types
from dotenv import load_dotenv
import os
import requests
from io import BytesIO
import markups

load_dotenv()

api_url = "https://cataas.com"
bot = TeleBot(os.getenv("BOT_TOKEN"))

@bot.message_handler(commands=["start"])
def start(message: types.Message):
    bot.send_message(message.chat.id, "А ты любишь котиков?", reply_markup=markups.markup)

@bot.message_handler(content_types=['text'], state=None)
def echo(message: types.Message):
    if message.text == "Дай котика":
        send_photo(message, requests.get(api_url + "/cat"))
    elif message.text == "Дай говорящего котика":
        msg = bot.send_message(message.chat.id, "Что скажет наш котик?")
        bot.register_next_step_handler(msg, take_text)
    else:
        bot.send_message(message.chat.id, message.text)

def take_text(message: types.Message):
    send_photo(message, requests.get(f"{api_url}/cat/says/{message.text}"))

def send_photo(message: types.Message, response: requests.Response):
    if response:
        bot.send_photo(message.chat.id, BytesIO(response.content))
    else:
        bot.send_message(message.chat.id, "Ошибка, котиков пока не будет")

if __name__ == "__main__":
    print("Start")
    bot.polling(True)