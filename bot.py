#!/usr/bin/python

# Write your Telegram bot
import os
import telebot

API_KEY = os.getenv ('TELEGRAM_TOKEN')

@bot.messege_handler(commands=['Greet'])
def Greet(message):
  bot.replay_to(message, "Hey! How R U?")

bot.polling()
