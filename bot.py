from telegram import Update
from telegram.ext import Application, CommandHandler

BOT_TOKEN = os.environ.get('BOT_TOKEN', 'YOUR_TOKEN_HERE')

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
