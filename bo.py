import telebot

# تۆکنی بۆتەکەت کە دابووت
TOKEN = "8911566349:AAEu0zIGfppWLAnEnfJqVphb158nG_8SO4o"
bot = telebot.TeleBot(TOKEN)


# وەڵامدانەوە بۆ فەرمانی /start یان هەر نامەیەک بە "سلاو"
@bot.message_handler(func=lambda message: True)
def send_hello(message):
  bot.reply_to(message, "سلاو")


# دەستپێکردنی بۆتەکە و وەستاندن لە چاوەڕوانیدا
print("بۆتەکە سەرکەوتووانە دەستی بە کارکردن کرد...")
bot.infinity_polling()
