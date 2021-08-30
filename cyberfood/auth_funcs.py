import telebot
import os



class AuthFunc:
    def __init__(self, bot):
        self.bot = bot

    def landing_body(self, message):
        resp = """
            <b>Hello, Welcome to CyberSpace Ghana</b>
        Let us help you get the food of your choice right away !
        Select an Option:
        1. Sign In to Your Account - /login
        2. Sign Up Account - /register
        3. Forgot Password - /forgot
        """
        self.bot.send_message(message.chat.id, resp)

    
    def login_body(self, message, func):
        resp = """
        <b>Kindly enter your username and pin...
        Separate them with a single space..</b>
        <i>Eg. uname 23445</i>
        """
        msg = self.bot.reply_to(message, resp)
        self.bot.register_next_step_handler(msg, func)
    
    def register_body(self, message, register):
        resp = """
        <b>Enter the info on a line each</b>
        <p>Full Name:</p>
        <p>Phone:</p>
        <p>Hostel:</p>
        <p>Room Number:</p>
        <p>Username:</p>
        Enter the details the way it is written
        """
        msg = self.bot.send_message(message.chat.id, resp)
        self.bot.register_next_step_handler(msg, register)