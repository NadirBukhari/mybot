import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# --- Configuration ---
# 1. REPLACE THIS TOKEN WITH YOUR BOT's TOKEN
BOT_TOKEN = "7964520765:AAEPO_AbqbB08E5bREn0QkkYpSb0gH3ASaQ"

# --- Set up logging to see errors ---
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# --- This function runs when a user sends /start ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a photo from a URL with a welcome caption and 7 inline buttons."""
    
    # 2. EDIT THE BUTTONS BELOW
    # Replace the channel names and URLs with your own.
    keyboard = [
        [InlineKeyboardButton("Channel 1 Name", url="https://t.me/your_channel_link_1")],
        [InlineKeyboardButton("Channel 2 Name", url="https://t.me/your_channel_link_2")],
        [InlineKeyboardButton("Channel 3 Name", url="https://t.me/your_channel_link_3")],
        [InlineKeyboardButton("Channel 4 Name", url="https://t.me/your_channel_link_4")],
        [InlineKeyboardButton("Channel 5 Name", url="https://t.me/your_channel_link_5")],
        [InlineKeyboardButton("Channel 6 Name", url="https://t.me/your_channel_link_6")],
        [InlineKeyboardButton("Channel 7 Name", url="https://t.me/your_channel_link_7")],
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # 3. REPLACE THIS WITH A DIRECT URL TO YOUR IMAGE
    # The image must be accessible via a public link.
    image_url = "https://i.postimg.cc/NM3qV5gX/image.png"

    # Your welcome message, which will be the image caption.
    welcome_caption = "<b>👋 Welcome to CB Access Vault </b> \n\n Here’s your private gateway to our <b> premium network. </b> \n\n Choose what you want to <b> access below 👇 </b>"
    
    # Send the photo using the URL with the caption and buttons.
    await update.message.reply_photo(
        photo=image_url,
        caption=welcome_caption, 
        reply_markup=reply_markup, 
        parse_mode="HTML"
    )

# --- Main function to set up and run the bot ---
def main() -> None:
    """Start the bot."""
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))

    print("Bot is running... Press Ctrl-C to stop.")
    application.run_polling()

if __name__ == "__main__":
    main()
