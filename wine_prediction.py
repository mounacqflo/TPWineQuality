import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDClassifier
from pandas import json_normalize
from os.path import exists
import joblib

from models.wine import Wine

N_ESTIMATOR = 400

def predictWine(wine: Wine):
    if exists("./rf.joblib"):
        rfc = joblib.load("./rf.joblib")
        del wine.wine['quality']
        new_wine = json_normalize(wine.wine)
        pred_rfc = rfc.predict(new_wine)
        return {"predict" : pred_rfc[0], "wine": wine.wine}
    else:
        return {"error" : "No predictor loaded. Please retrain."}

def retrain():
    data = pd.read_csv("Wines.csv")
    del data['Id']
    X = data.drop('quality', axis=1)
    y = data['quality']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)
    rfc = RandomForestClassifier(n_estimators=N_ESTIMATOR)
    rfc.fit(X_train, y_train)
    joblib.dump(rfc, "./rf.joblib")
    return {"message": "Successful retrain."}

def addWine(wine: Wine):
    # Vérifier avant que le quality n'est pas None
    data = pd.read_csv("Wines.csv")
    maxId = data['Id'].max()
    wine.wine['quality'] = 5
    wine.wine['Id'] = maxId+1
    new_data = pd.DataFrame.from_dict([wine.wine])
    data = data.append(new_data, ignore_index=True)
    data.to_csv("Wines.csv", index=False)
    return {"message": "Wine added in csv file."}

def description():
    if exists("./rf.joblib"):
        rfc = joblib.load("./rf.joblib")
    else:
        return {"error" : "No predictor loaded. Please retrain."}

#w = Wine(7.4, 0.7, 0, 1.9, 0.076, 11, 34, 0.9978, 3.51, 0.56, 9.4)
w = Wine(10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10)
"""print(w.wine)
print(predictWine(w))
print(retrain())"""
addWine(w)