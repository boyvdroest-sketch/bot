from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.environ.get('BOT_TOKEN', 'YOUR_TOKEN_HERE')

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🟡️ Join Channel 🟡️", url="https://t.me/senseiRedirect")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    message = """
Welcome to our Travel Deals Bot, Sensei Reloaded 🟡!

✗ Get ready for amazing travel deals and exclusive offers!

📌 Join our channel for the latest updates:  
https://t.me/senseiRedirect

Start your journey with us! 🟡️
    """
    await update.message.reply_text(
        message, 
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )

if __name__ == '__main__':
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start_command))
    print("Bot is running...")
    app.run_polling()
