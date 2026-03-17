from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from commands import start
from buttons import language_button, menu_button, catalog_button
from env import TOKEN

app = ApplicationBuilder().token(TOKEN).build()

# start command
app.add_handler(CommandHandler("start", start))

# language selector
app.add_handler(CallbackQueryHandler(language_button, pattern="^(lang_en|lang_ru|lang_es)$"))

# main menu buttons
app.add_handler(CallbackQueryHandler(menu_button, pattern="^(catalog|prices|how_to_buy|contacts|back_menu)$"))

# catalog categories
app.add_handler(CallbackQueryHandler(catalog_button, pattern="^(new_jerseys|retro_jerseys|shorts)$"))

app.run_polling()