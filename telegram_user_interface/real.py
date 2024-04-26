import telebot
from telebot import types

import os


class Bot:
    def __init__(self):
        # Variables
        self.token = "6045979402:AAEPHUbVZZQu_w_gIo-ybxNNVtzbM0s_Xp8"
        self.bot = telebot.TeleBot(self.token)
        self.user_state = dict()

        Bot.create_dir_for_csv_files()

        @self.bot.message_handler(commands=["start", "websites", "work_description", "delete_websites", "delete_work_description"])
        def get_info(msg: types.Message):
            if msg.text == "/start":
                self.bot.send_message(msg.chat.id, "This bot will help you find open vacancies")
            elif msg.text == "/websites":
                self.bot.reply_to(msg, "Write different website: \"site.com, site.com, site.com\"")
                self.user_state[msg.chat.id] = "websites"
            elif msg.text == "/work_description":
                self.bot.reply_to(msg, "Write description of what kind of work you are looking for")
                self.user_state[msg.chat.id] = "work description"
            elif msg.text == "/delete_websites":
                try:
                    open('../../telegramBot/csv_files/websites.csv', 'w').close()
                except:
                    pass
                self.bot.send_message(msg.chat.id, "Info was successfully deleted")
            elif msg.text == "/delete_work_description":
                try:
                    open('../../telegramBot/csv_files/work_description.txt', 'w').close()
                except:
                    pass
                self.bot.send_message(msg.chat.id, "Info was successfully deleted")

        @self.bot.message_handler(func=lambda callback: True)
        def write_info(msg: types.Message):
            if self.user_state.get(msg.chat.id, False) == "websites":
                with open("./csv_files/websites.csv", "w") as file:
                    file.write(msg.text)
                self.bot.send_message(msg.chat.id, "Successfully written to websites.csv")
                self.user_state.clear()

            elif self.user_state.get(msg.chat.id, False) == "work description":
                with open("./csv_files/work_description.txt", "w") as file:
                    file.write(msg.text)
                self.bot.send_message(msg.chat.id, "Successfully written to work_description.txt")
                self.user_state.clear()

    @staticmethod
    def create_dir_for_csv_files():
        # Create dir for csv files
        directory = "csv_files"
        current_path = os.getcwd()
        new_path = os.path.join(current_path, directory)
        os.makedirs(new_path, exist_ok=True)

    def run(self):
        self.bot.infinity_polling()


bot = Bot()
bot.run()