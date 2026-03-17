from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton("English 🇬🇧", callback_data="lang_en"),
            InlineKeyboardButton("Русский 🇷🇺", callback_data="lang_ru")
        ]
    ]

    await update.message.reply_text(
        "🌍 Choose language / Выберите язык",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )