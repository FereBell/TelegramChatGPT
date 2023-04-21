import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

mensajes = [{"role": "system", "content": "Asistente de para escribir artículos cientificos"}]


async def ChatQuestion(update: Update, context: ContextTypes.DEFAULT_TYPE) :
    mensaje = update.message.text
    mensajes.append({"role": "user", "content": mensaje})
    chat= openai.ChatCompletion.create(model="gpt-3.5-turbo", messages= mensajes)
    await context.bot.send_message(chat_id=update.effective_chat.id, text= chat.choices[0].message.content)
    mensajes.append({"role": "assistant", "content": chat.choices[0].message.content})


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    startString = 'Hola soy tu bot personal \n puedes preguntarme lo que sea'
    await context.bot.send_message(chat_id= update.effective_chat.id, text= startString)

if __name__ == '__main__':
    application = ApplicationBuilder().token('6060346663:AAFL3s1t0-DQV6IfwYEgsjlqZ8Rvl9k7lv4').build()
    openai.api_key = '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'

    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT, ChatQuestion))
    
    application.run_polling()