import pandas as pd
import numpy as np
from collections import Counter
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn import svm
from sklearn import model_selection
from sklearn.externals import joblib
from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt
import pickle as pkl

# saving the path of .sav files
path = "Predictor/"

# Reading DataFrame and removing columns
df = pd.read_csv("../Breast Cancer Dataset/data.csv", header=0)
del df['Unnamed: 32']
del df['id']

# Generating X and Y
y = df.values[:, 0]
x = df.values[:, 1:]
u = []
for i in y:
    if(i == 'M'):
        u.append(1)
    else:
        u.append(0)
y = np.array(u)
print np.shape(y)

# Splitting data for training and testing
X_train, X_test, y_train, y_test = model_selection.train_test_split(
    x, y, test_size=0.33, random_state=0)  # ,stratify = y)
print Counter(y_test), Counter(y_train)

filenames = ['dt.sav', 'rf_entropy.sav', 'et_entropy.sav',
             'rf_gini.sav', 'et_gini.sav']
modelnum = 0
# Training and evaluating Decision Tree
dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)
print "decision tree: ", dt.score(X_test, y_test)

pkl.dump(dt,
         open(path + filenames[modelnum], 'wb'))

modelnum = modelnum + 1
# Training and evaluating Random Forest and Extra Trees
for cri in ["entropy", "gini"]:

    rf = RandomForestClassifier(
        n_estimators=200, max_features=6, criterion=cri)
    rf.fit(X_train, y_train)
    pkl.dump(rf,
             open(path + filenames[modelnum], 'wb'))
    print "Random forest (", "with :", cri, ")", rf.score(X_test, y_test)
    modelnum = modelnum + 1
    et = ExtraTreesClassifier(n_estimators=200, max_features=6, criterion=cri)
    et.fit(X_train, y_train)
    pkl.dump(et,
             open(path + filenames[modelnum], 'wb'))
    print "Extra trees (", "with :", cri, ")", et.score(X_test, y_test)
    modelnum = modelnum + 1

"""
# ANALYSING FEATURE IMPORTANCES USING FOREST OF TREES.
# Build a forest and compute the feature importances

forest = ExtraTreesClassifier(n_estimators=250,
                              random_state=0)

forest.fit(df,y)

importances = forest.feature_importances_
std = np.std([tree.feature_importances_ for tree in forest.estimators_],
             axis=0)
indices = np.argsort(importances)[::-1]

# Print the feature ranking
print("Feature ranking:")

for f in range(df.shape[1]):
    print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))

# Plot the feature importances of the forest
plt.figure()
plt.title("Feature importances")
plt.bar(range(df.shape[1]), importances[indices],
       color="r", yerr=std[indices], align="center")
plt.xticks(range(df.shape[1]), indices,rotation='vertical')
plt.xlim([-1, df.shape[1]])
plt.show()

del df['diagnosis']
#Getting the average values of each column of the dataframe.
for i in range(0,df.shape[1]):
 print "i : ",i," ",np.mean(df[df.columns[i]]),"\n"
"""
