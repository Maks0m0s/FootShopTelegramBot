from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes


# ---------- LANGUAGE SELECT ----------
async def language_button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.data == "lang_en":
        context.user_data["lang"] = "en"
        await send_menu(query, "en")

    elif query.data == "lang_ru":
        context.user_data["lang"] = "ru"
        await send_menu(query, "ru")


# ---------- MAIN MENU ----------
async def send_menu(query, lang="en"):

    if lang == "ru":

        keyboard = [
            [InlineKeyboardButton("📦 Каталог", callback_data="catalog")],
            [InlineKeyboardButton("💰 Цены", callback_data="prices")],
            [InlineKeyboardButton("🛒 Как купить", callback_data="how_to_buy")],
            [InlineKeyboardButton("📞 Контакты", callback_data="contacts")]
        ]

        text = (
            "⚽ *FOOTSHOP*\n"
            "━━━━━━━━━━━━━━\n"
            "Магазин футбольных джерси\n\n"
            "✔ Высокое качество\n"
            "✔ Имя и номер бесплатно\n"
            "✔ Доставка по всему миру 🌍\n\n"
            "Выберите раздел:"
        )

    else:

        keyboard = [
            [InlineKeyboardButton("📦 Catalog", callback_data="catalog")],
            [InlineKeyboardButton("💰 Prices", callback_data="prices")],
            [InlineKeyboardButton("🛒 How To Buy", callback_data="how_to_buy")],
            [InlineKeyboardButton("📞 Contacts", callback_data="contacts")]
        ]

        text = (
            "⚽ *FOOTSHOP*\n"
            "━━━━━━━━━━━━━━\n"
            "Premium Football Jerseys Store\n\n"
            "✔ High Quality Jerseys\n"
            "✔ Custom Name & Number FREE\n"
            "✔ Worldwide Shipping 🌍\n\n"
            "Choose an option below:"
        )

    await query.edit_message_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )


# ---------- MAIN MENU BUTTONS ----------
async def menu_button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    lang = context.user_data.get("lang", "en")

    # ---------- CATALOG ----------
    if query.data == "catalog":

        if lang == "ru":

            keyboard = [
                [InlineKeyboardButton("🔥 Новые Джерси", callback_data="new_jerseys")],
                [InlineKeyboardButton("⭐ Ретро Джерси", callback_data="retro_jerseys")],
                [InlineKeyboardButton("⚡ Шорты", callback_data="shorts")],
                [InlineKeyboardButton("⬅ Назад", callback_data="back_menu")]
            ]

            text = (
                "📦 *КАТАЛОГ FOOTSHOP*\n"
                "━━━━━━━━━━━━━━\n"
                "Выберите категорию:"
            )

        else:

            keyboard = [
                [InlineKeyboardButton("🔥 New Jerseys", callback_data="new_jerseys")],
                [InlineKeyboardButton("⭐ Retro Jerseys", callback_data="retro_jerseys")],
                [InlineKeyboardButton("⚡ Shorts", callback_data="shorts")],
                [InlineKeyboardButton("⬅ Back", callback_data="back_menu")]
            ]

            text = (
                "📦 *FOOTSHOP CATALOG*\n"
                "━━━━━━━━━━━━━━\n"
                "Choose a category:"
            )

        await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")


    # ---------- PRICES ----------
    elif query.data == "prices":

        keyboard = [
            [InlineKeyboardButton("⬅ Back", callback_data="back_menu")]
        ]

        if lang == "ru":

            text = (
                "💰 *ЦЕНЫ*\n"
                "━━━━━━━━━━━━━━\n\n"
                "👕 *Новые Джерси*\n"
                "Fan версия — 25$\n"
                "Player версия — 35$\n\n"
                "⭐ *Ретро Джерси*\n"
                "Fan версия — 30$\n"
                "Player версия — 40$\n\n"
                "⚡ *Шорты*\n"
                "Fan версия — 15$\n"
                "Player версия — 25$\n\n"
                "🎁 Имя и номер — БЕСПЛАТНО\n"
                "       Доставка — БЕСПЛАТНО"
            )

        else:

            text = (
                "💰 *PRICES*\n"
                "━━━━━━━━━━━━━━\n\n"
                "👕 *New Jerseys*\n"
                "Fan Version — 25$\n"
                "Player Version — 35$\n\n"
                "⭐ *Retro Jerseys*\n"
                "Fan Version — 30$\n"
                "Player Version — 40$\n\n"
                "⚡ *Shorts*\n"
                "Fan Version — 15$\n"
                "Player Version — 25$\n\n"
                "🎁 Custom name & number — FREE\n"
                "       Shipping — FREE"
            )

        await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")


    # ---------- HOW TO BUY ----------
    elif query.data == "how_to_buy":

        keyboard = [
            [InlineKeyboardButton("📦 Catalog", callback_data="catalog")],
            [InlineKeyboardButton("⬅ Back", callback_data="back_menu")]
        ]

        if lang == "ru":

            text = (
                "🛒 *КАК КУПИТЬ*\n"
                "━━━━━━━━━━━━━━\n\n"
                "1️⃣ Перейдите в каталог\n"
                "2️⃣ Выберите джерси\n"
                "3️⃣ Сделайте скриншот\n"
                "4️⃣ Отправьте продавцу:\n\n"
                "• Фото\n"
                "• Размер\n"
                "• Имя и номер (по желанию)"
            )

        else:

            text = (
                "🛒 *HOW TO BUY*\n"
                "━━━━━━━━━━━━━━\n\n"
                "1️⃣ Go to catalog\n"
                "2️⃣ Choose the jersey\n"
                "3️⃣ Take screenshot\n"
                "4️⃣ Send seller:\n\n"
                "• Photo\n"
                "• Size\n"
                "• Custom name & number"
            )

        await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")


    # ---------- CONTACTS ----------
    elif query.data == "contacts":

        keyboard = [
            [InlineKeyboardButton("📸 Instagram", url="https://instagram.com/footshop2026")],
            [InlineKeyboardButton("💬 Telegram Seller", url="https://t.me/footshop_support")],
            [InlineKeyboardButton("⬅ Back", callback_data="back_menu")]
        ]

        if lang == "ru":

            text = (
                "📞 *КОНТАКТЫ*\n"
                "━━━━━━━━━━━━━━\n\n"
                "Instagram: @footshop2026\n"
                "Telegram продавец: @footshop_support"
            )

        else:

            text = (
                "📞 *CONTACTS*\n"
                "━━━━━━━━━━━━━━\n\n"
                "Instagram: @footshop2026\n"
                "Telegram Seller: @footshop_support"
            )

        await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="HTML")


    elif query.data == "back_menu":
        await send_menu(query, lang)


# ---------- CATALOG ----------
async def catalog_button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    lang = context.user_data.get("lang", "en")

    if query.data == "new_jerseys":

        text = "🔥 *New Jerseys*" if lang == "en" else "🔥 *Новые Джерси*"

        await query.edit_message_text(
            f"{text}\n\n📂 Open catalog:",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📂 Open Catalog", url="https://baocheng3f888.x.yupoo.com/categories/3517272")],
                [InlineKeyboardButton("⬅ Back", callback_data="catalog")]
            ]),
            parse_mode="Markdown"
        )

    elif query.data == "retro_jerseys":

        text = "⭐ *Retro Jerseys*" if lang == "en" else "⭐ *Ретро Джерси*"

        await query.edit_message_text(
            f"{text}\n\n📂 Open catalog:",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📂 Open Catalog", url="https://baocheng3f888.x.yupoo.com/categories/4803333")],
                [InlineKeyboardButton("⬅ Back", callback_data="catalog")]
            ]),
            parse_mode="Markdown"
        )

    elif query.data == "shorts":

        text = "⚡ *Football Shorts*" if lang == "en" else "⚡ *Футбольные Шорты*"

        await query.edit_message_text(
            f"{text}\n\n📂 Open catalog:",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📂 Open Catalog", url="https://baocheng3f888.x.yupoo.com/categories/5146701")],
                [InlineKeyboardButton("⬅ Back", callback_data="catalog")]
            ]),
            parse_mode="Markdown"
        )