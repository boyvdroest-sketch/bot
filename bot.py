from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
import os
import sys
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Secure: read the bot token from an environment variable instead of hard-coding it
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
if not BOT_TOKEN:
    logger.error("TELEGRAM_BOT_TOKEN environment variable is not set.")
    sys.exit(1)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Guard in case update.message is None for some update types
    if update.message is None:
        return

    keyboard = [
        [InlineKeyboardButton("🟡️ Join Channel 🟡️", url="https://t.me/flights_half_off")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    message = (
        "🟡 Welcome to Spidy's World – Where Trust Meets Incredible Savings! 🟡\n\n"
        "We know it sounds too good to be true. That’s why we’re building a trusted service you can rely on.\n\n"
        "Experience 50% Off on a World of Services: ✨\n\n"
        "• Travel: ✈️ Flights, 🏨 Hotels, 🚗 Rentals, 🚁 Helicopters\n"
        "• Lifestyle: 🍽️ Dining, 🎫 Events, 🎢 Six Flags, 🛒 Groceries\n"
        "• Essentials: 🚆 Train Passes, 💳 Bills, 🎓 School Fees, 🏥 Hospital Bills\n\n"
        "One Platform. Endless Possibilities. Real Savings.\n\n"
        "We’re your one-stop partner for making your money go further.\n\n"
        "Ready to unlock your deals?\n"
        "Join our official channel to get started\n"
        "With trust,\n"
        "Your Friend, @yrfrnd_spidy\n"
    )

    await update.message.reply_text(
        message,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


def main():
    # Build the application with the token from env
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start_command))

    logger.info("Bot is starting (polling)...")
    # Use drop_pending_updates to avoid processing a backlog and reduce
    # chance of conflicts on startup; this is helpful if getUpdates
    # backlog or a previous instance exists.
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
