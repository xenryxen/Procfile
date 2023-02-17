import telebot
import time

bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def welcome(message):
    # send welcome message with "Continue" button
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = telebot.types.KeyboardButton('Начать')
    markup.add(button)
    bot.send_message(message.chat.id, 'Привет, чтобы узнать <b>с кем переписывался человек,</b> жми начать', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Continue')
def ask_name(message):
    # ask for person's name
    markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "Enter person's name", reply_markup=markup)
    bot.register_next_step_handler(message, ask_date)

def ask_date(message):
    # ask for date
    name = message.text
    bot.send_message(message.chat.id, "Enter date")
    bot.register_next_step_handler(message, perform_analysis, name)

def perform_analysis(message, name):
    # perform analysis
    date = message.text
    bot.send_message(message.chat.id, "Analysis...")
    time.sleep(2)
    bot.send_message(message.chat.id, "Got it...")
    time.sleep(2)
    bot.send_message(message.chat.id, "Done...")
    time.sleep(2)
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = telebot.types.KeyboardButton('Sign up')
    markup.add(button)
    bot.send_message(message.chat.id, "To continue subscribe...", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Sign up')
def ask_check(message):
    # ask for check
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = telebot.types.KeyboardButton('Check')
    markup.add(button)
    bot.send_message(message.chat.id, "Can't see...", reply_markup=markup)
    bot.register_next_step_handler(message, say_fine)

def say_fine(message):
    # say fine
    markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "Fine...", reply_markup=markup)

bot.polling()
