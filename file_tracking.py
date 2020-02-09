from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os
import telebot
from telebot import apihelper
from conf import TOKEN, proxy, chat_id, split_chr, path

apihelper.proxy = {'https': proxy}
bot = telebot.TeleBot(TOKEN)


def send_message(*args):
    message = args[0]
    bot.send_message(chat_id, message)


class Handler(FileSystemEventHandler):
    def on_created(self, event):
        if os.path.isfile(event.src_path):
            print(event.src_path.split(split_chr)[-1])
            send_message(event.src_path.split('\\')[-1])


@bot.message_handler(commands=['start'])
def send_echo(message):
    bot.send_message(message.chat.id, 'Работаю')


if __name__ == '__main__':
    observer = Observer()
    observer.schedule(Handler(), path=path, recursive=True)
    observer.start()
    bot.send_message(chat_id, 'Бот запущен')
    bot.polling()
