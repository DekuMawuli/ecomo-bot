from telebot import types as t
import telebot
import os

bot = telebot.TeleBot(os.getenv("ALPHABOT_KEY"), parse_mode="HTML")


def launch_screen():
    markup = t.InlineKeyboardMarkup()
    markup.add(t.InlineKeyboardButton(text="Login", callback_data="login"))
    markup.add(t.InlineKeyboardButton(text="Register", callback_data="register"))
    markup.add(t.InlineKeyboardButton(text="Forgot Password", callback_data="forgot"))
    return markup


