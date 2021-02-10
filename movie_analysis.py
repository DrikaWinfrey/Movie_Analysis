# -*- coding: utf-8 -*-
"""Movie_Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VDV_n-pi3gQZRXvJhTeuzI9P8ZTtzXho
"""

# Commented out IPython magic to ensure Python compatibility.
# %pylab inline
import warnings
warnings.filterwarnings('ignore')

from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, f1_score

import cloudpickle as cp
from urllib.request import urlopen
dataset = cp.load(urlopen("https://drive.google.com/uc?export=download&id=1tqjekAEy_SM_sJUvjIBbajp6I-_WmHgj"))

print(len(dataset.target))
print(dataset.data[220])

docs_train, docs_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=0.25, random_state=123)

#TfidfVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
tf = TfidfVectorizer()
docs_train = tf.fit_transform(docs_train)

docs_test = tf.transform(docs_test)

#SVC model
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
scores = []
for c in [0.01, 0.1, 1, 10]:
    model = SVC(kernel = 'rbf', C=c)
    model.fit(docs_train, y_train)

    y_pred = model.predict(docs_test)
    score = accuracy_score(y_test, y_pred)
    scores.append(score)
print(scores)

#Naive Bayes
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB()
clf.fit(docs_train, y_train)
y_pred = clf.predict(docs_test)
score = accuracy_score(y_test, y_pred)
print('MultinomialNB: ' + str(score))

#Random forest model
from sklearn.ensemble import RandomForestClassifier
scores = []
for c in [20, 100, 500]:
    clf = RandomForestClassifier(n_estimators = c)    
    clf.fit(docs_train, y_train)    
    y_pred = clf.predict(docs_test)
    score = accuracy_score(y_test, y_pred)
    scores.append(score)
print(scores)