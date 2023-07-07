import sys
import textwrap
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def generate_balloon(text):
    lines = text.split("\n")
    max_length = max(len(line) for line in lines)
    balloon = []
    balloon.append(" " + "_" * (max_length + 2))
    for line in lines:
        balloon.append("< {} >".format(line.ljust(max_length)))
    balloon.append(" " + "-" * (max_length + 2))
    return balloon

def cowsay(text, eyes_option="sad"):
    # eyes = get_eyes(eyes_option)
    balloon = generate_balloon(text)
    output = []
    output.append("{}".format("".join(balloon)))
    output.append("{}".format(r'        \   ^__^'))
    output.append("{}".format(r'         \  (oo)\_______'))
    # output.append("{}".format(r'         \  ({})\_______'.format(eyes)))
    output.append("{}".format(r'            (__)\       )\/\\'))
    output.append("{}".format(r'                ||----w |'))
    output.append("{}".format(r'                ||     ||'))
    return "\n".join(output)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # define some things

    ## get input message from telegram user
    user_input = update.message.text
    command = '/vacas'  # Change this to the appropriate command
    message_text = user_input.replace(command, '').strip()

    cow_message = cowsay(message_text)

    response = f"```\n{cow_message}\n```"  # Enclose the cow message in triple backticks to preserve formatting

    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=response,
        parse_mode='Markdown'
    )

if __name__ == '__main__':
    application = ApplicationBuilder().token('6139722782:AAF5oXTywXGxEtBapHAC7mAtklCY-0I6nEc').build()
    
    start_handler = CommandHandler('vacas', start)
    application.add_handler(start_handler)
    
    application.run_polling()