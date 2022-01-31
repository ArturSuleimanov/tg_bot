from qr_code_gen import qr_code_generator
import telebot
import os


class Token:
    __access = '5028283661:AAFET5yE8oanFFe-AlUu-vI6l8p1GOm-vGk'   # Access token for my tg bot


    @classmethod
    def acces_get(cls):    # Getter for __access of <class 'Token'>
        '''
        :return: __access
        '''
        return cls.__access


class Bot:
    bot = telebot.TeleBot(Token.acces_get())

    @classmethod
    def start_message(cls, message):      # How to reply to command
        cls.bot.send_message(message.chat.id, "Hi, let's get it started. Send me your link")


    @classmethod
    def send_qr(cls, link):
        '''
        Takes link, send qr, deletes image
        :param link: link you need to convert
        :return: None
        '''
        file_name = qr_code_generator(link.text)
        cls.bot.send_photo(link.from_user.id, open(file_name, 'rb'))
        os.remove(file_name)


@Bot.bot.message_handler(commands=['start'])    # Reply to command /start
def start_message(message):
    Bot.start_message(message)

@Bot.bot.message_handler(content_types=['text'])    # Converts link
def send_photo(message):
    Bot.send_qr(message)


Bot.bot.polling()    # Always scanning for new messages
