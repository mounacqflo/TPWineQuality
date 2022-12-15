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

class WinePrediction:
    def __init__(self):
        pass

    def convertWineToDict(self, wine: Wine):
        d = {}
        d["fixed acidity"] = wine.fixed_acidity
        d["volatile acidity"] = wine.volatile_acidity
        d["citric acid"] = wine.citric_acid
        d["residual sugar"] = wine.residual_sugar
        d["chlorides"] = wine.chlorides
        d["free sulfur dioxide"] = wine.free_sulfur_dioxide
        d["total sulfur dioxide"] = wine.total_sulfur_dioxide
        d["density"] = wine.density
        d["pH"] = wine.pH
        d["sulphates"] = wine.sulphates
        d["alcohol"] = wine.alcohol
        d["quality"] = wine.quality
        return d

    def predictWine(self, wine: Wine):
        w = self.convertWineToDict(wine)
        if exists("./rf.joblib"):
            rfc = joblib.load("./rf.joblib")
            del w["quality"]
            new_wine = json_normalize(w)
            pred_rfc = rfc.predict(new_wine)
            print(pred_rfc)
            #return {"predict" : str(pred_rfc[0]), "wine": w}
            return {"predict" : str(pred_rfc[0])}
        else:
            return {"error" : "No predictor loaded. Please retrain."}

    def retrain(self):
        data = pd.read_csv("Wines.csv")
        del data['Id']
        X = data.drop('quality', axis=1)
        y = data['quality']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)
        rfc = RandomForestClassifier(n_estimators=400)
        rfc.fit(X_train, y_train)
        joblib.dump(rfc, "./rf.joblib")
        return {"message": "Successful retrain."}

    def addWine(self, wine: Wine):
        # VÃ©rifier avant que le quality n'est pas None
        w = self.convertWineToDict(wine)
        data = pd.read_csv("Wines.csv")
        maxId = data['Id'].max()
        w['Id'] = maxId+1
        new_data = pd.DataFrame.from_dict([w])
        data = data.append(new_data, ignore_index=True)
        data.to_csv("Wines.csv", index = False)
        return {"message": "Wine added in csv file."}

    def bestWine(self):
        data = pd.read_csv("Wines.csv")
        data = data.sort_values(by=['quality'], ascending=False)
        wine = data.iloc[0]
        return {
            "fixed acidity": wine["fixed acidity"],
            "volatile acidity": wine["volatile acidity"],
            "citric acid": wine["citric acid"],
            "residual sugar": wine["residual sugar"],
            "chlorides": wine["chlorides"],
            "free sulfur dioxide": wine["free sulfur dioxide"],
            "total sulfur dioxide": wine["total sulfur dioxide"],
            "density": wine["density"],
            "pH": wine["pH"],
            "sulphates": wine["sulphates"],
            "alcohol": wine["alcohol"],
            "quality": wine["quality"]
        }

    def description(self):
        if exists("./rf.joblib"):
            rfc = joblib.load("./rf.joblib")
            data = pd.read_csv("Wines.csv")
            del data['Id']
            X = data.drop('quality', axis=1)
            y = data['quality']
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)
            desc = rfc.get_params()
            desc["accuracy"] = round(rfc.score(X_test, y_test),3)
            return desc
        else:
            return {"error" : "No predictor loaded. Please retrain."}