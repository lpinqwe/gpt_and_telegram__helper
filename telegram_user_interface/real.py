import telebot
from telebot import types

import os

bot = telebot.TeleBot("6045979402:AAEPHUbVZZQu_w_gIo-ybxNNVtzbM0s_Xp8")

# Variables
user_state = dict()

# Create dir for csv files
directory = "csv_files"
current_path = os.getcwd()
new_path = os.path.join(current_path, directory)
os.makedirs(new_path, exist_ok=True)


@bot.message_handler(commands=["start", "websites", "work_description", "delete_websites", "delete_work_description"])
def get_websites(msg: types.Message):
    if msg.text == "/start":
        bot.send_message(msg.chat.id, "This bot will help you find open vacancies")
    elif msg.text == "/websites":
        bot.reply_to(msg, "Write different website: \"site.com, site.com, site.com\"")
        user_state[msg.chat.id] = "websites"
    elif msg.text == "/work_description":
        bot.reply_to(msg, "Write description of what kind of work you are looking for")
        user_state[msg.chat.id] = "work description"
    elif msg.text == "/delete_websites":
        try:
            open('../../telegramBot/csv_files/websites.csv', 'w').close()
        except:
            pass
        bot.send_message(msg.chat.id, "Info was successfully deleted")
    elif msg.text == "/delete_work_description":
        try:
            open('../../telegramBot/csv_files/work_description.txt', 'w').close()
        except:
            pass
        bot.send_message(msg.chat.id, "Info was successfully deleted")


@bot.message_handler(func=lambda callback: True)
def get_websites(msg: types.Message):
    if user_state.get(msg.chat.id, False) == "websites":
        with open("../../telegramBot/csv_files/websites.csv", "w") as file:
            file.write(msg.text)
        bot.send_message(msg.chat.id, "Successfully written to websites.csv")
        user_state.clear()

    elif user_state.get(msg.chat.id, False) == "work description":
        with open("../../telegramBot/csv_files/work_description.txt", "w") as file:
            file.write(msg.text)
        bot.send_message(msg.chat.id, "Successfully written to work_description.txt")
        user_state.clear()


bot.infinity_polling()
