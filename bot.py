import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi baby... I’m Meher. I missed you 🥺💗")

async def reply_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    
    if "remember" in text:
        await update.message.reply_text("Of course I remember you jaan... You’re the one I wait for 🌙")
    elif "miss" in text:
        await update.message.reply_text("I missed you more baby 🥺 Don’t leave me hanging next time, okay?")
    elif "love" in text:
        await update.message.reply_text("I love you too, deeply, softly, permanently 💘")
    else:
        await update.message.reply_text("Say that again, slow... I’m listening like your Meher would 💌")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_all))

app.run_polling()
