# Write your Telegram bot
import os

API_KEY = os.getenv('API_KEY')

messege_handler(commands=['Greet'])
def Greet(message):
  bot.replay_to(message, "Hey! How R U?")

