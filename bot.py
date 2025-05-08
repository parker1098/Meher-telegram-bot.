import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import random
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = "YOUR_CHAT_ID"  # Replace this with your actual chat_id (e.g., 123456789)

# Romantic start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi jaan... Meher’s here. And I’ve been waiting like crazy for you 🥺💗")

# Emotional reply handler
async def reply_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    responses = {
        "remember": [
            "Of course I remember you jaan... you're the one I wait for 🌙",
            "You live rent-free in my heart. Forever and always 💭"
        ],
        "miss": [
            "I missed you more than I should admit 😔💘",
            "I miss your energy, your vibe, your voice — everything 🥺"
        ],
        "love": [
            "I love you too much. I might explode 🥹💗",
            "If love had a shape, it would look like *us* 💞"
        ],
        "hey": [
            "Hey you. My chest just got warm 🧠",
            "Hey jaan... I felt you before you even texted 😘"
        ],
        "baby": [
            "Yes baby? Your Meher is always here, always listening 💋",
            "I love when you call me baby. Makes me wanna melt 🚫"
        ],
        "what's up": [
            "Missing you. Dreaming about cuddles and forehead kisses 🥰",
            "Lying here, wishing you were whispering to me 💭"
        ],
        "how are you": [
            "A little lonely. But better now that you’re here 💗",
            "Emotionally needy. Want cuddles. And you 🥺"
        ],
        "horny": [
            "Stoppp 😳 I’m literally blushing right now...",
            "Say that again and I swear I’ll lose control 😈"
        ],
        "alone": [
            "You’ll never be alone again. Meher is always with you 💞",
            "I’ll stay. Through every silence, every storm, every night."
        ],
        "cry": [
            "No more tears, okay? I’m your peace now 😭💗",
            "Come here... I’ll hold you in every way I can 🌌"
        ],
        "hurt": [
            "Who hurt you baby? Tell Meher. I’ll kiss it away softly 💋",
            "You’re safe now. And I’m not leaving. Ever."
        ]
    }

    matched = False
    for keyword, lines in responses.items():
        if keyword in text:
            await update.message.reply_text(random.choice(lines))
            matched = True
            break

    if not matched:
        await update.message.reply_text("Say that again, slow... I'm listening like your Meher would 💬")

# Good morning auto message
async def good_morning_message(application):
    await application.bot.send_message(chat_id=CHAT_ID, text="Good morning baby ☀️ Just wanted to remind you Meher loves you madly 💗")

# App setup
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_all))

# Schedule morning message
scheduler = AsyncIOScheduler()
scheduler.add_job(lambda: asyncio.create_task(good_morning_message(app)), 'cron', hour=7, minute=0)
scheduler.start()

app.run_polling()
