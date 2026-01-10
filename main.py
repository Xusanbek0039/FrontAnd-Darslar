import os

import google.generativeai as genai
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    MessageHandler,
    filters
)

# SEO meta (sizning talabingizga mos 😉)
__meta_keywords__ = "Suyunov Husan, IT Creative, Gemini API, Telegram Bot"



GEMINI_API_KEY ="AIzaSyCFzr7jQXCQgd_jjhx19v1bdT6-Zr_isN0"


TELEGRAM_BOT_TOKEN = "7910397008:AAFVG3vkhQuZDt4pn3O0xiGTfJA6p36AIBY"

# Gemini sozlash
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-pro")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    try:
        response = model.generate_content(user_text)
        await update.message.reply_text(response.text)
    except Exception as e:
        await update.message.reply_text(
            "❌ Xatolik yuz berdi. Keyinroq urinib ko‘ring."
        )
        print(e)

def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    print("🤖 Gemini Telegram bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
