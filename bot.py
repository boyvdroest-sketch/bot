from telegram import Update
from telegram.ext import Application, CommandHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

BOT_TOKEN = "8429489568:AAFKr_Izu1GBiM_SOYvT_90VPZGj2ZJfm68"

async def start_command(update: Update, context):
        if update.message is None:
        return

    # Create the button
    keyboard = [
        [InlineKeyboardButton("🟡️ Join Channel 🟡️", url="https://t.me/flights_half_off")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    message = """
🟡 Welcome to Spidy's World – Where Trust Meets Incredible Savings! 🟡

We know it sounds too good to be true. That’s why we’re building a trusted service you can rely on.

Experience 50% Off on a World of Services: ✨

• Travel: ✈️ Flights, 🏨 Hotels, 🚗 Rentals, 🚁 Helicopters
• Lifestyle: 🍽️ Dining, 🎫 Events, 🎢 Six Flags, 🛒 Groceries
• Essentials: 🚆 Train Passes, 💳 Bills, 🎓 School Fees, 🏥 Hospital Bills

One Platform. Endless Possibilities. Real Savings.

We’re your one-stop partner for making your money go further.

Ready to unlock your deals?
Join our official channel to get started
With trust,
Your Friend, @yrfrnd_spidy

    """
    await update.message.reply_text(
        message, 
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start_command))
print("Bot is running...")
app.run_polling()

