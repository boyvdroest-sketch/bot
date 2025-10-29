from telegram import Update
from telegram.ext import Application, CommandHandler

BOT_TOKEN = "8429489568:AAFKr_Izu1GBiM_SOYvT_90VPZGj2ZJfm68"

async def start_command(update: Update, context):
    message = """
Welcome to our Travel Deals Bot, Spidy's World 🟡!

✗ Get ready for amazing travel deals and exclusive offers!

📌 Join our channel for the latest updates:  
https://t.me/flights_half_off
Start your journey with us! 🟡️

🟡️ Join Channel 🟡️
    """
    await update.message.reply_text(message)

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start_command))
print("Bot is running...")
app.run_polling()