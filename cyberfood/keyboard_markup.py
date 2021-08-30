from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import telebot
import os

bot = telebot.TeleBot(os.getenv("ALPHABOT_KEY"), parse_mode="HTML")


def launch_screen():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(
        InlineKeyboardButton("Login", callback_data="cb_login"),
        InlineKeyboardButton("Register", callback_data="cb_reg"),
        InlineKeyboardButton("Forgot Password", callback_data="cb_forgot"),
    )
    return markup


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    print(call)
    if call.data == "cb_login":
        bot.answer_callback_query(call.id, "Answer is Yes")
    elif call.data == "cb_reg":
        bot.answer_callback_query(call.id, "Answer is No")
    elif call.data == "cb_forgot":
        bot.answer_callback_query(call.id, "Answer is forgot")
