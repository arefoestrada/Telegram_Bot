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

# Variabel i digunakan sebagai variabel iteratif dalam looping dan tidak bermakna apapun selain itu
i = 0

# Looping untuk menentukan respons atas input yang diberikan oleh user
while i < 100:
	u = input()
	i += 1
	L = []

	# Setiap input yang diberikan oleh user dimasukkan ke dalam list L, lalu di-transform dan diprediksi oleh model
	L.append(u)
	ut = loaded_model1.transform(L)
	kat = loaded_model2.predict(ut)

	# Berbagai kondisi yang muncul sebagai respons dari input user
	if kat == t_0:
		print('Ada yang bisa dibantu?')
	elif kat == t_1:
		print('Semoga harimu menyenangkan!')
		break
	elif kat == t_2:
		print('My pleasure!')
		break
	elif kat == t_3:
		print('Jam kerja kami adalah jam 9.00 sampai 21.00')
	elif kat == t_4:
		print('Saat ini, kami menyediakan Jeep, Innova, dan Avanza')
	elif kat == t_5:
		print('Kami menerima pembayaran menggunakan Visa, Mastercard, dan AMEX')
	elif kat == t_6:
		print('Jam kerja kami adalah jam 9.00 sampai 21.00')
	elif kat == t_7:
		print('Kapan mau sewa?')
	elif kat == t_8:
		print('Untuk penyewaan hari ini, hubungi 081315995534')
	else:
		print('Maaf, aku belum mengerti hua :(')