import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# --- Configuration ---
# The bot token is now loaded securely from an environment variable.
# You will set this variable on the hosting platform (Railway).
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# --- Set up logging to see errors ---
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# --- This function runs when a user sends /start ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a photo from a URL with a welcome caption and buttons."""
    
    # Your button configuration with your links
    keyboard = [
        [InlineKeyboardButton("📡 CB Network", url="https://t.me/+-xENE63Gjps0Y2Zh")],
        [InlineKeyboardButton("🎓 Premium Courses", url="https://t.me/+GMQ2Wa4MF2cxNDM8")],
        [InlineKeyboardButton("📦 Methods & Resources", url="https://t.me/+buk6EurNwmlhYThk")],
        [InlineKeyboardButton("💹 Trading Signals", url="https://t.me/cb_traders1")],
        [InlineKeyboardButton("🌟 Future Stars", url="https://t.me/Future_stars_Army")],
        [InlineKeyboardButton("🎁 Udemy Courses", url="https://t.me/udemy_free_coupns")],
        [InlineKeyboardButton("🔐 VIP Membership", url="https://t.me/+SFBgzlVEZcs0OTg8")],
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Your image URL
    image_url = "https://i.postimg.cc/NM3qV5gX/image.png"

    # Your image caption
    welcome_caption = "<b>👋 Welcome to CB Access Vault </b> \n\n Here’s your private gateway to our <b> premium network. </b> \n\n Choose what you want to <b> access below 👇 </b>"
    
    # Send the photo with the caption and buttons
    await update.message.reply_photo(
        photo=image_url,
        caption=welcome_caption, 
        reply_markup=reply_markup, 
        parse_mode="HTML"
    )

# --- Main function to set up and run the bot ---
def main() -> None:
    """Start the bot."""
    # Add a check to ensure the token was loaded
    if not BOT_TOKEN:
        print("Error: BOT_TOKEN environment variable not set!")
        return
        
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
