from keep_alive import keep_alive
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Получаем токен из переменных окружения
TOKEN = os.getenv('TOKEN')


# Функция на команду /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🚨 Фишка ➡️", callback_data='fishka')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("🚨 Фишка ➡️", reply_markup=reply_markup)


# Функция при нажатии кнопки
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    await context.bot.send_message(chat_id=query.message.chat.id,
                                   text="ФИШКА!!!")


# Запуск бота
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler('start', start))
app.add_handler(CallbackQueryHandler(button))

keep_alive()
print("Бот запущен!")
app.run_polling()
