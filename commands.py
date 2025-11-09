from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Shop 🛒", callback_data="shop")],
        [InlineKeyboardButton("Prices 💰", callback_data="prices")],
        [InlineKeyboardButton("Help ❓", callback_data="help")],
        [InlineKeyboardButton("About Us ℹ️", callback_data="about")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "\tWelcome to FootShop !!!\nChoose your option :",
        reply_markup=reply_markup
    )