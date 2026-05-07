from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

API_ID = int(os.getenv("19907816"))
API_HASH = os.getenv("87a3fb970ec190dd9cb07ad0d225d912")
BOT_TOKEN = os.getenv("8247813428:AAFi3RCCdlkA2QcQOLd11QyjTcC4Ag4uSBY")

app = Client(
    "report_tracker_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client, message):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Spam", callback_data="spam"),
            InlineKeyboardButton("Scam", callback_data="scam")
        ]
    ])

    await message.reply(
        "ارسل يوزر الانستا بعدين اختار السبب",
        reply_markup=keyboard
    )

@app.on_callback_query()
async def callback(client, query):
    await query.message.reply(
        f"تم حفظ البلاغ: {query.data}"
    )

app.run()
