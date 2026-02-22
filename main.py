import telebot
from flask import Flask
from threading import Thread
import time

# ১. আপনার বটের টোকেন এখানে বসান
API_TOKEN = 'YOUR_BOT_TOKEN_HERE'
bot = telebot.TeleBot(API_TOKEN)

# ২. রেন্ডার (Render) সার্ভারকে সচল রাখার জন্য ওয়েব সার্ভার সেটআপ
app = Flask('')

@app.route('/')
def home():
    return "Bot is running 24/7 on Render!"

def run():
    # রেন্ডার সাধারণত ৮0৮0 পোর্ট ব্যবহার করে
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# ৩. আপনার বটের লজিক বা কমান্ড এখানে শুরু হবে
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "হ্যালো! আমি রেন্ডার সার্ভার থেকে লাইভ আছি।")

# আপনার আগের তৈরি করা সব ফিচার (যেমন টাইমার বা ডিলিট) এখানে নিচের লাইনে পেস্ট করুন:
# [এখানে আপনার বাকি কোড পেস্ট করুন]

# ৪. বট চালু করার ফাইনাল অংশ
if __name__ == "__main__":
    try:
        keep_alive() # সার্ভারকে ঘুমাতে দেবে না
        print("Bot is successfully running...")
        bot.infinity_polling()
    except Exception as e:
        print(f"Error occurred: {e}")
        time.sleep(5)
