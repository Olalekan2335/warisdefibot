import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler

# Configuration - using your testing token directly
TOKEN = '7745409076:AAHTmAVAim4cVxH0p8Da-z527JPR0z095O4'
CHANNEL_USERNAME = "@yourchannel"  # Change this to your actual channel
GROUP_USERNAME = "@yourgroup"     # Change this to your actual group
TWITTER_USERNAME = "yourtwitter"   # Change this to your actual Twitter

# Start command - first interaction with the bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    welcome_text = f"""
🌟 *Welcome to Our Airdrop Program*, {user.first_name}! 🌟

To qualify for *10 SOL* airdrop, please complete these simple steps:

1️⃣ Join our official channel: {CHANNEL_USERNAME}
2️⃣ Join our community group: {GROUP_USERNAME}
3️⃣ Follow us on Twitter: https://twitter.com/{TWITTER_USERNAME}

After completing all tasks, simply send your *Solana wallet address* here!

🔥 *Limited time offer!* 🔥
"""
    
    # Create interactive buttons
    keyboard = [
        [InlineKeyboardButton("📢 Join Channel", url=f"https://t.me/{CHANNEL_USERNAME[1:]}")],
        [InlineKeyboardButton("👥 Join Group", url=f"https://t.me/{GROUP_USERNAME[1:]}")],
        [InlineKeyboardButton("🐦 Follow Twitter", url=f"https://twitter.com/{TWITTER_USERNAME}")],
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode='Markdown')

# Handle wallet address submission
async def handle_wallet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    
    # Basic Solana wallet format check (very simple validation)
    if len(text) >= 32 and len(text) <= 44:
        congrats_text = """
🎉 *CONGRATULATIONS!* 🎉

Your submission has been received!

✅ *10 SOL* will be sent to your wallet within 24 hours.

Thank you for participating in our airdrop program!
"""
        await update.message.reply_text(congrats_text, parse_mode='Markdown')
    else:
        await update.message.reply_text("⚠️ Please enter a *valid Solana wallet address* (32-44 characters).", parse_mode='Markdown')

# Error handler
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")

def main():
    print("Starting bot...")
    
    # Create application with your token
    application = Application.builder().token(TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_wallet))
    
    # Error handler
    application.add_error_handler(error)
    
    # Start polling
    print("Polling...")
    application.run_polling()

if __name__ == "__main__":
    main()
