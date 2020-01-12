# Untuk mengimpor file dalam format json
import json
data = json.load(open('data.json'))

import numpy as np
import pandas as pd

# Memisahkan data patterns untuk setiap tag ke dalam list yang berbeda-beda
p_0 = data['pengetahuan'][0]['patterns']
p_1 = data['pengetahuan'][1]['patterns']
p_2 = data['pengetahuan'][2]['patterns']
p_3 = data['pengetahuan'][3]['patterns']
p_4 = data['pengetahuan'][4]['patterns']
p_5 = data['pengetahuan'][5]['patterns']
p_6 = data['pengetahuan'][6]['patterns']
p_7 = data['pengetahuan'][7]['patterns']
p_8 = data['pengetahuan'][8]['patterns']

# Memisahkan data tag
t_0 = data['pengetahuan'][0]['tag']
t_1 = data['pengetahuan'][1]['tag']
t_2 = data['pengetahuan'][2]['tag']
t_3 = data['pengetahuan'][3]['tag']
t_4 = data['pengetahuan'][4]['tag']
t_5 = data['pengetahuan'][5]['tag']
t_6 = data['pengetahuan'][6]['tag']
t_7 = data['pengetahuan'][7]['tag']
t_8 = data['pengetahuan'][8]['tag']

# Membuat satu list terintegrasi yang berisi semua patterns
X = []
import itertools
for p in itertools.chain(p_0, p_1, p_2, p_3, p_4, p_5, p_6, p_7, p_8):
    X.append(p)

# Membuat satu list terintegrasi yang berisi semua tag yang disesuaikan dengan jumlah patterns yang ada
y = []
for t in range(len(p_0)):
    y.append(t_0)
for t in range(len(p_1)):
    y.append(t_1)
for t in range(len(p_2)):
    y.append(t_2)
for t in range(len(p_3)):
    y.append(t_3)
for t in range(len(p_4)):
    y.append(t_4)
for t in range(len(p_5)):
    y.append(t_5)
for t in range(len(p_6)):
    y.append(t_6)
for t in range(len(p_7)):
    y.append(t_7)
for t in range(len(p_8)):
    y.append(t_8)

# Mengimpor tfidf untuk mengekstraksi teks
from sklearn.feature_extraction.text import TfidfVectorizer
vect = TfidfVectorizer()

X_vect = vect.fit_transform(X)

from sklearn.svm import LinearSVC
model = LinearSVC(max_iter=1000000)

model.fit(X_vect, y)

# Mengimpor pickle untuk yang pertama agar model bag of words tersimpan
import pickle
nama_model = 'model1.pkl'
pickle.dump(vect, open(nama_model,'wb'))

# Mengimpor pickle untuk yang kedua agar model machine learning untuk prediksi tersimpan
import pickle
nama_model = 'model2.pkl'
pickle.dump(model, open(nama_model,'wb'))