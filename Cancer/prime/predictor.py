import pickle as pkl
import numpy
import pandas
import sys
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
import os
import warnings
path = "prime/Predictor/"
models = {'dt.sav': "Decision Tree", 'rf_entropy.sav': "Random Forest. Criterion : Entropy", 'rf_gini.sav': "Random Forest. Criterion : Gini",
          'et_entropy.sav': "Extra Trees. Criterion : Entropy", 'et_gini.sav': "Random Forest. Criterion : Gini"}
result = {0: "Benign", 1: "Malignant"}


def predictCancer(X):  # X is an 1D array with the features of the cancer cell
    global path, models
    # print os.getcwd()
    # print X.shape
    answer = 0  # answer is a voting variable
    totalprob = 0
    for i in models:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
        model = pkl.load(open(path + i, 'rb     '))
        pred = model.predict(X)[0]
        totalprob = totalprob + model.predict_proba(X)[0][0]
        print models[i].ljust(40), ":", result[pred]
        # Malignant gets a +1 vote and Benign gets a -1 vote
        answer = answer + (1 if(pred) else -1)

    totalprob = totalprob / len(models)

    if(answer > 0):
        return totalprob, "Malignant"
    else:
        return totalprob, "Benign"
