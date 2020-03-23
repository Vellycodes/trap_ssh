import telebot
import config
import os
import threading
class bott(threading.Thread):
    def run(self):
            print('bot on')
            bot = telebot.TeleBot(config.tgtoken)
            @bot.message_handler(commands=['ban'])
            def handle_text(message):
                    msg = str(message.text).split(' ')
                    if len(msg) > 1:
                        datebase.ban_ip(ip=msg[1])


            @bot.message_handler(commands=['ban_never'])
            def handle_text(message):
                    msg = str(message.text).split(' ')
                    if len(msg) > 1:
                        os.system("sudo iptables -A INPUT -s" + msg[1] + " -j DROP")


            @bot.message_handler(commands=['unban'])
            def handle_text(message):
                    msg = str(message.text).split(' ')
                    if len(msg) > 1:
                        os.system("sudo iptables -D INPUT -s " + msg[1] + " -j DROP")
            bot.polling(none_stop=True,timeout=30)
