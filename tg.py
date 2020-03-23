import config
import telebot
import os
bot = telebot.TeleBot(config.tgtoken)
def alert(text):
    bot.send_message(chat_id=config.root_bot,
                                 text=text)
