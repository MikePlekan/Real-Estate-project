import pandas as pd
import utils as utils
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.neural_network import MLPClassifier
from sklearn import tree
from sklearn import metrics
from sklearn import preprocessing

df=utils.get_df('./zillowData/County_time_series.csv')
df=df.query("RegionName != 'United_States'")
df2=df[df.columns[list([0,1,2,6,7,8,9,10,11,21])]].dropna(axis=0)
lab = preprocessing.LabelEncoder()
dftransformed = lab.fit_transform(df2)
X_train, X_test, y_train, y_test = train_test_split(dftransformed[dftransformed.columns[list([0,1,2,3,4,5,6,7,8])]], dftransformed[dftransformed.columns[list([9])]], test_size=0.2, random_state=42)

clf = svm.SVC()

clf.fit(X_train, y_train)

predications = clf.predict(X_test)

accuracy = metrics.accuracy_score(y_test, predications)

print(f"accuracy: {accuracy:.2f}")