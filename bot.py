#!/usr/bin/python

# Write your Telegram bot
import os
import telebot

API_KEY = '7008948652:AAFoDBxL8KqeqM_tD_u1MPCy5Lb05wLymB8' #os.getenv ('TELEGRAM_TOKEN')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['Greet'])
def greet(message):
  bot.replay_to(message, "Hey! How R U?")

bot.polling()
