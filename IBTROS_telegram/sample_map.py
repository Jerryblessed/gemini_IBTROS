from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# Function to handle the /start command and display the inline keyboard
def start(update, context):
    keyboard = [[InlineKeyboardButton("Map", callback_data='map')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Click the button to view the map:', reply_markup=reply_markup)

# Function to handle the button click and send the map
def button_click(update, context):
    query = update.callback_query
    if query.data == 'map':
        map_html = """
        <iframe src="https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d1859.803694865057!2d7.426249575093579!3d8.991765163512934!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e6!4m5!1s0x104e732036038e5d%3A0xdb27d0b19f52c049!2sAldenco%20Estate%2C%20XCP9%2B7CG%2C%20Abuja%20900107%2C%20Federal%20Capital%20Territory!3m2!1d8.9857403!2d7.4185221!4m5!1s0x104e737ddb63ee91%3A0x6158fbea4b716e3c!2sDunamis%20International%20Gospel%20Centre%2C%20Galadimawa%2C%20XCQG%2BRPV%2C%201%20Dunamis%20church%2C%20galadimawa%2C%20Galadima!3m2!1d8.9891398!2d7.4270187!5e0!3m2!1sen!2sng!4v1701487905402!5m2!1sen!2sng"
        width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        """
        context.bot.send_message(chat_id=query.message.chat_id, text="Here's the map:")
        context.bot.send_message(chat_id=query.message.chat_id, text=map_html, parse_mode='HTML')

# Initialize the bot
updater = Updater('5244306869:AAFrJqdmrIpAbKx_HuSWBlhhYVsJEeIuShI', use_context=True)

# Set up handlers
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(button_click))

# Start the bot
updater.start_polling()
updater.idle()
