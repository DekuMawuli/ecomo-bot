from models import create_db
import telebot
import os
import time

bot = telebot.TeleBot(os.getenv("ALPHABOT_KEY"), parse_mode="HTML")


@bot.message_handler(commands=['start'])
def landing(message):
    resp = f"""
        <b>Hello Dear, Welcome to CyberSpace Ghana</b>
        Let us help you get the food of your choice right away !
        Select an Option:
        1. Login - /login
        2. Register - /register
        3. Forgot Pin - /forgot
    """
    bot.send_message(message.chat.id, resp)


@bot.message_handler(commands=['login'])
def login(message):
    resp = """
    <b>Kindly enter your username and pin...
    Separate them with a single space..</b>
    <i>Eg. uname 23445</i>
    """
    msg = bot.reply_to(message, resp)
    bot.register_next_step_handler(msg, get_user_credentials)


def get_user_credentials(message):
    try:
        chat_id = message.chat.id
        username, pwd = message.text.split(" ")
        print(f"Username: {username} & Password: {pwd}")
    except:
        bot.reply_to(message, "Something Went Wrong")

# =============================================


@bot.message_handler(commands=['forgot'])
def forgot_password(message):
    resp = """
    <b>Kindly Enter your Email to receive a token</b>
    """
    msg = bot.reply_to(message, resp)
    bot.register_next_step_handler(msg, forgot_pwd)


def forgot_pwd(message):
    try:
        chat_id = message.chat.id
        email = message.text
        msg = bot.reply_to(message, f"Enter Token Sent to {email}: ")
        bot.register_next_step_handler(msg, verify_token)
    except:
        bot.reply_to(message, "Something Went Wrong")


def verify_token(message):
    try:
        chat_id = message.chat.id
        token = message.text
        while token != "2468mawuli":
            msg = bot.reply_to(message, "Enter correct token")
            bot.register_next_step_handler(msg, verify_token)
            return
        bot.reply_to(message, "Verified Hurray")

    except:
        bot.reply_to(message, "Something Went Wrong")


if __name__ == '__main__':
    create_db()
    while True:
        try:
            bot.polling()
        except Exception as e:
            time.sleep(15)
