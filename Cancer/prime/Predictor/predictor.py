import pickle
import numpy,pandas
import sys
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier

def predictCancer(X):   #X is an 1D array with the features of the cancer cell

    answer = 0     #answer is a voting variable
    
    for i in ['dt.sav','rf_entropy.sav','rf_gini.sav','et_entropy.sav','et_gini.sav']:
        model = pkl.load(open(i,'rb'))
        answer = answer + (1 if(model.predict(X)[0]) else -1)  #Malignant gets a +1 vote and Benign gets a -1 vote

    if(answer>0):
        return "Malignant"
    else:
        return "Benign"
    

