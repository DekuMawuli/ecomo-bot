from cyberfood.models import create_db
import telebot
import os
from cyberfood.auth_funcs import AuthFunc


bot = telebot.TeleBot(os.getenv("ALPHABOT_KEY"), parse_mode="HTML")
authViews = AuthFunc(bot)


@bot.message_handler(commands=['start'])
def landing(message):
    authViews.landing_body(message)


@bot.message_handler(commands=["login"])
def login(message):
    authViews.login_body(message,get_user_credentials)


def get_user_credentials(message):
    if "/register" in message.text:
        authViews.register_body(message, verify_and_register_user)
    elif "/" in message.text:
        authViews.landing_body(message)
    else:
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
    <b>Kindly Enter your Email: </b>
    """
    msg = bot.reply_to(message, resp)
    bot.register_next_step_handler(msg, forgot_pwd)


def forgot_pwd(message):
    if "/" in message.text:
        authViews.landing_body(message)
    else:
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

# =============== REGISTER ROUTE


@bot.message_handler(commands=['register'])
def register(message):
    authViews.register_body(message, verify_and_register_user)


def verify_and_register_user(message):
    try:
        chat_id = message.chat.id
        print(message.text)
        bot.send_message(message.chat.id, "Info Received")
    except:
        bot.reply_to(message, "Something Went Wrong")


if __name__ == '__main__':
    create_db()
    bot.polling(none_stop=True)
