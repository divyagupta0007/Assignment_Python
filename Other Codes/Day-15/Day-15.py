print("*****************************************EVALUATING A BASE CLASSIFIER*****************************************")

import sys

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets

data = datasets.load_wine(as_frame=True)

x = data.data
y = data.target

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.25, random_state=46)

dtree = DecisionTreeClassifier(random_state=46)
dtree.fit(x_train, y_train)

y_pred = dtree.predict(x_test)

print("Train data Accuracy Score: ", accuracy_score(y_true=y_train, y_pred=dtree.predict(x_train)))
print("Test data Accuracy Score: ", accuracy_score(y_true=y_test, y_pred=y_pred))


print("*****************************************CREATING A BAGGING CLASSIFIER*****************************************")

import matplotlib.pyplot as plt
from sklearn.ensemble import BaggingClassifier

data = datasets.load_wine(as_frame=True)

x = data.data
y = data.target

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.25, random_state=46)

estimator_range = [2,4,6,8,10,12,14,16]

models = []
scores = []

for n_estimators in estimator_range:

    clf = BaggingClassifier(n_estimators=n_estimators, random_state=46)
    clf.fit(x_train, y_train)

    models.append(clf)
    scores.append(accuracy_score(y_true=y_test, y_pred=clf.predict(x_test)))

plt.figure(figsize=(9,6))
plt.plot(estimator_range, scores)

plt.xlabel("n_estimators", fontsize=18)
plt.ylabel("Scores", fontsize=18)
plt.tick_params(labelsize=16)

plt.show()


print("*****************************************GENERATING DECISION TREES FROM BAGGING CLASSIFIER*****************************************")

from sklearn.tree import plot_tree

x = data.data
y = data.target

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.25, random_state=46)

clf = BaggingClassifier(n_estimators=12, oob_score=True, random_state=46)

clf.fit(x_train, y_train)

plt.figure(figsize=(20,10))
plot_tree(clf.estimators_[0], feature_names = x.columns)
plt.show()


print("*****************************************IMPLEMENTING XGBOOST*****************************************")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import seaborn as sns
import xgboost as xgb
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

import os
os.environ["PATH"] += os.pathsep + r'C:\Program Files\Graphviz\bin'


sns.set_style("whitegrid")

df = pd.read_csv("Day-15\Wholesale-customers-data.csv")

print(df.head())

print("\n\nStatistical Summary")

print(df.describe())

x = df.drop("Channel", axis=1)
y = df["Channel"].map({1:1, 2:0})

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

params = {

    "objective" : "binary:logistic",
    "max_depth" : 4,
    "learning_rate" : 0.1,
    "n_estimators" : 100,
    "alpha" : 10 

}

model = XGBClassifier(**params)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print("Model Accuracy: ", accuracy_score(y_test, y_pred))
print("Classification Report: ", classification_report(y_test, y_pred))

plt.figure(figsize=(5, 4))
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

plt.figure(figsize=(5, 6))
xgb.plot_importance(model)
plt.title("Feature Importance")
plt.show()

plt.figure(figsize=(20, 10))
xgb.plot_tree(model)
