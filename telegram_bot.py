# Mengimpor package Telegram yang digunakan
from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram import ReplyKeyboardMarkup

# Melakukan loading untuk model bag of words
import pickle
nama_model1 = 'model1.pkl' #sesuai dengan nama file yang di simpan
loaded_model1 = pickle.load(open(nama_model1, 'rb'))

# Melakukan loading untuk machine learning yang akan memprediksi
import pickle
nama_model2 = 'model2.pkl' #sesuai dengan nama file yang di simpan
loaded_model2 = pickle.load(open(nama_model2, 'rb'))

# Mengimpor file json untuk mengambil data tag
import json
data = json.load(open('data.json'))

import numpy as np

t_0 = np.array(data['pengetahuan'][0]['tag'])
t_1 = np.array(data['pengetahuan'][1]['tag'])
t_2 = np.array(data['pengetahuan'][2]['tag'])
t_3 = np.array(data['pengetahuan'][3]['tag'])
t_4 = np.array(data['pengetahuan'][4]['tag'])
t_5 = np.array(data['pengetahuan'][5]['tag'])
t_6 = np.array(data['pengetahuan'][6]['tag'])
t_7 = np.array(data['pengetahuan'][7]['tag'])
t_8 = np.array(data['pengetahuan'][8]['tag'])

# Mendefinisikan output ketika user mengetik /start di chatroom
def start(update, context):
	update.message.reply_text('Halo, ini adalah bot untuk memberikan informasi penyewaan mobil.')

# Menentukan respons chatbot dari setiap input yang diberikan oleh user
def echo(update, context):
		u = update.message.text
		L = []

		L.append(u)
		ut = loaded_model1.transform(L)
		kat = loaded_model2.predict(ut)

		if kat == t_0:
			update.message.reply_text('Ada yang bisa dibantu?')
		elif kat == t_1:
			update.message.reply_text('Semoga harimu menyenangkan!')
			L = []
		elif kat == t_2:
			update.message.reply_text('My pleasure!')
			L = []
		elif kat == t_3:
			update.message.reply_text('Jam kerja kami adalah jam 9.00 sampai 21.00')
		elif kat == t_4:
			update.message.reply_text('Saat ini, kami menyediakan Jeep, Innova, dan Avanza')
		elif kat == t_5:
			update.message.reply_text('Kami menerima pembayaran menggunakan Visa, Mastercard, dan AMEX')
		elif kat == t_6:
			update.message.reply_text('Jam kerja kami adalah jam 9.00 sampai 21.00')
		elif kat == t_7:
			update.message.reply_text('Kapan mau sewa?')
		elif kat == t_8:
			update.message.reply_text('Untuk penyewaan hari ini, hubungi 081315995534')
		else:
			update.message.reply_text('Maaf, aku belum mengerti hua :(')

import config

updater = Updater(config.updater, use_context = True)

dp = updater.dispatcher
dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.text, echo))

# Starting the bot
updater.start_polling()
updater.idle()