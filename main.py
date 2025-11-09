from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from commands import start
from buttons import start_button, shop_button, prices_button

app = ApplicationBuilder().token("8223990252:AAEZRpsYXWb2oaaCGOLcYVzxXbMHxVC2PhI").build()

# Command handler
app.add_handler(CommandHandler("start", start))

# Callback query handlers with patterns
app.add_handler(CallbackQueryHandler(start_button, pattern="^(shop|prices|help|about)$"))
app.add_handler(CallbackQueryHandler(shop_button, pattern="^(new_jerseys_s|retro_jerseys_s|shorts_s)$"))
app.add_handler(CallbackQueryHandler(prices_button, pattern="^(new_jerseys_p|retro_jerseys_p|shorts_p)$"))

app.run_polling()