# Write your Telegram bot
import os
import telebot

API_KEY = os.getenv('API_KEY')

@bot.messege_handler(commands=['Greet'])
def greet(message):
  bot.replay_to(message, "Hey! How R U?")

