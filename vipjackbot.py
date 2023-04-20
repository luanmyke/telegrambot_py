import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import CallbackQueryHandler, CommandHandler, Filters, MessageHandler, Updater

TOKEN = "5818928337:AAF-yeseyx_rkT0r13gXrKqvN42m0ylEmFY"

# Read allowed users from file
with open('allowed_users.txt', 'r') as f:
    allowed_users = [line.strip() for line in f.readlines()]


def send_message():
    bot = telegram.Bot(TOKEN)
    buttons = [
        InlineKeyboardButton(text="CRASH 🚀", callback_data="crash"),
        InlineKeyboardButton(text="MINES 💣", callback_data="mines"),
        InlineKeyboardButton(text="GOAL 🥅", callback_data="goal"),
    ]
    keyboard = InlineKeyboardMarkup([buttons])
    photo_url = "https://freeimage.host/i/HvM15Ja"
    message = '''
    <b>BEM-VINDOS AO MENU DE ROBÔS DO GRUPO JACK.
    EM QUAL DE NOSSOS SERVIÇOS VOCÊ QUER LUCRAR?</b>
    '''
    message = bot.send_photo(chat_id="-1001817225721", photo=photo_url, caption=message, reply_markup=keyboard, parse_mode=ParseMode.HTML)
    return message


def button_callback(update, context):
    query = update.callback_query
    print(query)
    user_id = query.from_user.id
    if str(user_id) not in context.bot_data['allowed_users']:
        context.bot.send_message(chat_id=user_id, text="You are not authorized to use this service.")
        return
    query.answer()
    button = query.data
    if button == "crash":
        url = "https://t.me/crashbotSSS"
    elif button == "mines":
        url = "https://t.me/xminesgames"
    elif button == "goal":
        url = "https://t.me/sssgoaljack"
    context.bot.send_message(chat_id=query.message.chat_id, text=f"Opening {url}", disable_web_page_preview=True)


def main():
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.bot_data['allowed_users'] = allowed_users
    dispatcher.add_handler(CallbackQueryHandler(button_callback, pass_user_data=True))
    send_message()
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()