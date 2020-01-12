import json
data = json.load(open('data.json'))
import numpy as np
import pandas as pd

p_0 = data['pengetahuan'][0]['patterns']
p_1 = data['pengetahuan'][1]['patterns']
p_2 = data['pengetahuan'][2]['patterns']
p_3 = data['pengetahuan'][3]['patterns']
p_4 = data['pengetahuan'][4]['patterns']
p_5 = data['pengetahuan'][5]['patterns']
p_6 = data['pengetahuan'][6]['patterns']
p_7 = data['pengetahuan'][7]['patterns']
p_8 = data['pengetahuan'][8]['patterns']

t_0 = data['pengetahuan'][0]['tag']
t_1 = data['pengetahuan'][1]['tag']
t_2 = data['pengetahuan'][2]['tag']
t_3 = data['pengetahuan'][3]['tag']
t_4 = data['pengetahuan'][4]['tag']
t_5 = data['pengetahuan'][5]['tag']
t_6 = data['pengetahuan'][6]['tag']
t_7 = data['pengetahuan'][7]['tag']
t_8 = data['pengetahuan'][8]['tag']

X = []
import itertools
for p in itertools.chain(p_0, p_1, p_2, p_3, p_4, p_5, p_6, p_7, p_8):
    X.append(p)

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

from sklearn.feature_extraction.text import TfidfVectorizer
vect = TfidfVectorizer()

X_vect = vect.fit_transform(X)

from sklearn.svm import LinearSVC
model = LinearSVC(max_iter=1000000)

model.fit(X_vect, y)

import pickle
nama_model = 'model1.pkl'
pickle.dump(vect, open(nama_model,'wb'))

import pickle
nama_model = 'model2.pkl'
pickle.dump(model, open(nama_model,'wb'))