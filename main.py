import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from keep_alive import keep_alive

TOKEN = os.getenv('TOKEN')

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🚨 Фишка ➡️", callback_data='fishka')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    message = await update.message.reply_text("🚨 Фишка ➡️", reply_markup=reply_markup)

    # Ожидание 5 минут (300 секунд)
    await asyncio.sleep(3)

    # Попытка удалить сообщение
    try:
        await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=message.message_id)
    except Exception as e:
        print(f"Ошибка при удалении сообщения: {e}")

# Нажатие на кнопку
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    message = await context.bot.send_message(chat_id=query.message.chat_id, text="ФИШКА!!!")

    # Ожидание 5 минут (300 секунд)
    await asyncio.sleep(3)

    # Попытка удалить сообщение
    try:
        await context.bot.delete_message(chat_id=query.message.chat_id, message_id=message.message_id)
    except Exception as e:
        print(f"Ошибка при удалении сообщения: {e}")

# Запуск бота
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler('start', start))
app.add_handler(CallbackQueryHandler(button))

keep_alive()
print("Бот запущен!")
app.run_polling()
