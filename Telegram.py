from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters)

BTN_JAVA, BTN_JAVASCRIPT, BTN_PYTHON, BTN_C, BTN_HTML, BTN_CSS, BTN_AUTOCAD, BTN_3DSMAX, BTN_UNITY, BNT_ADOBE = ('Python asoslari', 'Algoritmlar', 'Web dasturlash', 'Pycharm', 'Telegram Bot', 'C tili', 'Qo\'shimcha ma\'lumotlar', 'Admin bilan bog\'lanish', 'Astrum bilan bo\'lanish', 'Adobe') 
main_buttons = ReplyKeyboardMarkup([
    [BTN_JAVA, BTN_JAVASCRIPT, BTN_PYTHON], [BTN_C, BTN_HTML, BTN_CSS], [BTN_AUTOCAD, BTN_3DSMAX, BTN_UNITY], [BNT_ADOBE]
], resize_keyboard=True)

STATE_REGION = 1
STATE_CALENDAR = 2

def start(update, context):
	user = update.message.from_user

	buttons = [
        [
        InlineKeyboardButton("Python asoslari", callback_data="1_dastur"),
        InlineKeyboardButton("Algoritmlar", callback_data="2_dastur"),
        ],
        [
        InlineKeyboardButton("Web dasturlash", callback_data="3_dastur"),
        InlineKeyboardButton("Pycharm", callback_data="4_dastur"),
        ],
        [
        InlineKeyboardButton("Telegram Bot", callback_data="5_dastur"),
        InlineKeyboardButton("C dasturlash tili", callback_data="6_dastur"),
        ],
        [
        InlineKeyboardButton("Qo'shimcha ma'lumotlar", callback_data="7_dastur"),
        InlineKeyboardButton("Admin bilan bog'lanish", callback_data="8_dastur"),
        ],
        [
        InlineKeyboardButton("Astrum bilan bog\'lanish", callback_data="9_dastur"),
        # InlineKeyboardButton("Adobe", callback_data="10_dastur")
        ]
	]
	
	update.message.reply_html("Salom <b>{}!</b>\n \n<b>Astrum Data Science botimizga xush kelibsiz</b>\n \n<b>Quyidagilardan birini tanlang: </b>".
		format(user.first_name), reply_markup=InlineKeyboardMarkup(buttons))

	return STATE_REGION

def inline_callback(update, context):
	try:
		query = update.callback_query
		query.message.delete()
		query.message.reply_html(text="\nQuyidagi bo'limlardan birini tanlang 👇", reply_markup=main_buttons)

		return STATE_CALENDAR
	except Exception as e:
		print("error ", str(e))

def Java(update, context):
	update.message.reply_text('Bu kanalda python sariq dev ning "Python asoslari" darslari bor: https://t.me/Python0050')

def JavaScript(update, context):
	update.message.reply_text('Bu kanalda sariq dev ning "Ma\'lumotlar tuzilmasi va algoritmlar bor" https://t.me/Python0051')

def Python(update, context):
	update.message.reply_text('Bu kanalda sariq dev ning "Python web dastrulash darslari bor": https://t.me/Python0052')

def C(update, context):
	update.message.reply_text('Bu kanalda "Pycharm" bo\'yicha ma\'lumotlar bor: https://t.me/Python0053')

def html(update, context):
	update.message.reply_text('Bu kanalda sariq dev ning "Mukammal telegram bot yaratish" bo\'yicha darslari bor: https://t.me/Python0054')

def CSS(update, context):
	update.message.reply_text('Bu kanalda "C" dasturlash tili asoslari bor: https://t.me/Python0056')

def AutoCad(update, context):
	update.message.reply_text('Bu kanalda "Python" bo\'yicha qo\'shimcha ma\'lumotlar bor: https://t.me/Python0055')

def DsMax(update, context):
	update.message.reply_text('Admin bilan bog\'lanish: \n'
							  '+998999986711 \n'
							  '+998338898041 \n'
							  'https://t.me/im_steve_johnson \n'
							  'https://t.me/Jasur77official')

def Unity(update, context):
	update.message.reply_text('Astrum bilan bog\'lanish: \n'
							  'https://t.me/astrumuz \n'
							  '+998712024222')

def Adobe(update, context):
	update.message.reply_text('Adobe darslar bu kanalda: https://t.me/joinchat/AAAAAEm8gYy3FQsPXLlTIA')									


def main():
	updater = Updater('2012695693:AAFcCEGJyfK5x4Cf1D6Y446jQJnvdnIkGa4', use_context=True)

	dispatcher = updater.dispatcher

	# dispatcher.add_handler(CommandHandler('start', start))

	# dispatcher.add_handler(CallbackQueryHandler(inline_callback))

	conv_handler = ConversationHandler(
		entry_points = [CommandHandler('start', start)],
		states={
		    STATE_REGION: [CallbackQueryHandler(inline_callback)],
		    STATE_CALENDAR:[
		    MessageHandler(Filters.regex('^('+BTN_JAVA+')$'), Java),
		    MessageHandler(Filters.regex('^('+BTN_JAVASCRIPT+')$'), JavaScript),
		    MessageHandler(Filters.regex('^('+BTN_PYTHON+')$'), Python),
		    MessageHandler(Filters.regex('^('+BTN_C+')$'), C),
		    MessageHandler(Filters.regex('^('+BTN_HTML+')$'), html),
		    MessageHandler(Filters.regex('^('+BTN_CSS+')$'), CSS),
		    MessageHandler(Filters.regex('^('+BTN_AUTOCAD+')$'), AutoCad),
		    MessageHandler(Filters.regex('^('+BTN_3DSMAX+')$'), DsMax),
		    MessageHandler(Filters.regex('^('+BTN_UNITY+')$'), Unity),
		    MessageHandler(Filters.regex('^('+BNT_ADOBE+')$'), Adobe)
		    ],
		},
		fallbacks=[CommandHandler('start', start)]
	
	)

	dispatcher.add_handler(conv_handler)

	updater.start_polling()
	updater.idle()

main()