from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton("English 🇬🇧", callback_data="lang_en"),
            InlineKeyboardButton("Русский 🇷🇺", callback_data="lang_ru"),
            InlineKeyboardButton("Español 🇪🇸", callback_data="lang_es")
        ]
    ]

    await update.message.reply_text(
        "🌍 Choose language / Выберите язык / Elige idioma",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )