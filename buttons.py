from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
import os

from db import new_jerseys, retro_jerseys, shorts

async def start_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "shop":
        keyboard = [
            [InlineKeyboardButton("New Jerseys", callback_data="new_jerseys_s")],
            [InlineKeyboardButton("Retro Jerseys", callback_data="retro_jerseys_s")],
            [InlineKeyboardButton("Football Shorts", callback_data="shorts_s")],
        ]
        await query.edit_message_text(
            "\t|\tSHOP\t|\t\nCategories :",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    elif query.data == "prices":
        keyboard = [
            [InlineKeyboardButton("New Jersey Price 💰", callback_data="new_jerseys_p")],
            [InlineKeyboardButton("Retro Jersey Price 💰", callback_data="retro_jerseys_p")],
            [InlineKeyboardButton("Shorts Price 💰", callback_data="shorts_p")],
        ]
        await query.edit_message_text("Choose items category :", reply_markup=InlineKeyboardMarkup(keyboard))
    elif query.data == "help":
        await query.edit_message_text("--- Bot Usage Instructions ---\n"
                                      "\t- /start : after sending this command you get all next functions of the bot :)\n"
                                      "\t- To contact us, use the next email : footshop15@gmail.com")
    elif query.data == "about":
        await query.edit_message_text("About Us :\n")
        await context.bot.send_message(chat_id=query.message.chat_id, text="We are a company of selling football items managed by Mr.Maks. Our start-up started in September of 2025, and if you are reading this text, we are still working ;)")


async def prices_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    chat_id = query.message.chat_id

    if query.data == 'new_jerseys_p':
        if len(new_jerseys) >= 1:
            prices = []
            for jersey in new_jerseys:
                prices.append(jersey['price'])
            middle_prices = sum(prices) / len(prices)
            await query.edit_message_text(text=f"New Jersey's Price : {middle_prices}€")
        else:
            await query.edit_message_text(text="No jerseys found.")
    if query.data == 'retro_jerseys_p':
        if len(retro_jerseys) >= 1:
            prices = []
            for jersey in retro_jerseys:
                prices.append(jersey['price'])
            middle_prices = sum(prices) / len(prices)
            await query.edit_message_text(text=f"Retro Jersey's Price : {middle_prices}€")
        else:
            await query.edit_message_text(text="No jerseys found.")
    if query.data == 'shorts_p':
        if len(shorts) >= 1:
            prices = []
            for short in shorts:
                prices.append(short['price'])
            middle_prices = sum(prices) / len(prices)
            await query.edit_message_text(text=f"Football Shorts Price : {middle_prices}€")
        else:
            await query.edit_message_text(text="No shorts found.")

async def shop_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    chat_id = query.message.chat_id

    if query.data == "new_jerseys_s":
        if len(new_jerseys) >= 1:
            await query.edit_message_text("New Jerseys :")
            for i, jersey in enumerate(new_jerseys):
                await context.bot.send_message(
                    chat_id=chat_id,
                    text=f"{i+1}. {jersey['club']} | {jersey['year']}"
                )

                photo_path = jersey['photo_url']
                if os.path.exists(photo_path):  # ✅ Use local file if available
                    with open(photo_path, "rb") as img:
                        details = ""
                        if len(jersey['details']) >= 1:
                            for detail in jersey['details']:
                                details += f'\n\t· {detail}'
                            await context.bot.send_photo(chat_id=chat_id, photo=img,
                                                         caption=f"✅ Details : {details}\nBrand : {jersey['brand']}\n💰 Price : {jersey['price']}€\n"
                                                                 f"🔗 <a href='{jersey['url']}'>Click here to view</a>", parse_mode="HTML")
                        else:
                            await context.bot.send_photo(chat_id=chat_id, photo=img,
                                                         caption=f"Brand : {jersey['brand']}\n💰 Price: {jersey['price']}€\n🔗 <a href='{jersey['url']}'>Click here to view</a>", parse_mode="HTML")
                else:
                    await context.bot.send_message(chat_id=chat_id, text="⚠️ Image not found.")
        else:
            await context.bot.send_message(chat_id=chat_id, text="No jerseys found.")

    elif query.data == "retro_jerseys_s":
        if len(retro_jerseys) >= 1:
            await query.edit_message_text("Retro Jerseys :")
            for i, r_jersey in enumerate(retro_jerseys):
                await context.bot.send_message(
                    chat_id=chat_id,
                    text=f"{i + 1}. {r_jersey['club']} | {r_jersey['year']}"
                )

                photo_path = r_jersey['photo_url']
                if os.path.exists(photo_path):  # ✅ Use local file if available
                    with open(photo_path, "rb") as img:
                        details = ""
                        if len(r_jersey['details']) >= 1:
                            for detail in r_jersey['details']:
                                details += f'\n\t· {detail}'
                            await context.bot.send_photo(chat_id=chat_id, photo=img,
                                                         caption=f"✅ Details : {details}\nBrand : {r_jersey['brand']}\n💰 Price: {r_jersey['price']}€\n🔗 <a href='{r_jersey['url']}'>Click here to view</a>", parse_mode="HTML")
                        else:
                            await context.bot.send_photo(chat_id=chat_id, photo=img,
                                                         caption=f"Brand : {r_jersey['brand']}\n💰 Price: {r_jersey['price']}€\n🔗 <a href='{r_jersey['url']}'>Click here to view</a>", parse_mode="HTML")
                else:
                    await context.bot.send_message(chat_id=chat_id, text="⚠️ Image not found.")
        else:
            await context.bot.send_message(chat_id=chat_id, text="No jerseys found.")

    elif query.data == "shorts_s":
        if len(shorts) >= 1:
            await query.edit_message_text("Football Shorts :")
            for i, short in enumerate(shorts):
                await context.bot.send_message(
                    chat_id=chat_id,
                    text=f"{i + 1}. {short['club']} | {short['year']}"
                )

                photo_path = short['photo_url']
                if os.path.exists(photo_path):  # ✅ Use local file if available
                    with open(photo_path, "rb") as img:
                        details = ""
                        if len(short['details']) >= 1:
                            for detail in short['details']:
                                details += f'\n\t· {detail}'
                            await context.bot.send_photo(chat_id=chat_id, photo=img,
                                                         caption=f"✅ Details : {details}\nBrand : {short['brand']}\n💰 Price: {short['price']}€\n🔗 <a href='{short['url']}'>Click here to view</a>", parse_mode="HTML")
                        else:
                            await context.bot.send_photo(chat_id=chat_id, photo=img,
                                                         caption=f"Brand : {short['brand']}\n💰 Price: {short['price']}€\n🔗 <a href='{short['url']}'>Click here to view</a>", parse_mode="HTML")
                else:
                    await context.bot.send_message(chat_id=chat_id, text="⚠️ Image not found.")
        else:
            await context.bot.send_message(chat_id=chat_id, text="No shorts found.")
