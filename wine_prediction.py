import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from pandas import json_normalize, Series
from os.path import exists
import joblib

from models.wine import Wine

class WinePrediction:
    def __init__(self):
        pass


    def convertWineIntoDict(self, wine: Wine):
        """ Convert a Wine model instance into a dictionnary. """

        wine_dict = {
            "fixed acidity": wine.fixed_acidity,
            "volatile acidity": wine.volatile_acidity,
            "citric acid": wine.citric_acid,
            "residual sugar": wine.residual_sugar,
            "chlorides": wine.chlorides,
            "free sulfur dioxide": wine.free_sulfur_dioxide,
            "total sulfur dioxide": wine.total_sulfur_dioxide,
            "density": wine.density,
            "pH": wine.pH,
            "sulphates": wine.sulphates,
            "alcohol": wine.alcohol,
            "quality": wine.quality
        }
        return wine_dict


    def convertPandaObjectIntoWine(self, wine_panda_object: Series):
        """ Convert a Series panda object into Wine a model instance. """

        return Wine(
            fixed_acidity = wine_panda_object["fixed acidity"], 
            volatile_acidity = wine_panda_object["volatile acidity"],
            citric_acid = wine_panda_object["citric acid"],
            residual_sugar = wine_panda_object["residual sugar"],
            chlorides = wine_panda_object["chlorides"],
            free_sulfur_dioxide = wine_panda_object["free sulfur dioxide"],
            total_sulfur_dioxide = wine_panda_object["total sulfur dioxide"],
            density = wine_panda_object["density"],
            pH = wine_panda_object["pH"],
            sulphates = wine_panda_object["sulphates"],
            alcohol = wine_panda_object["alcohol"],
            quality = wine_panda_object["quality"]
        )


    def predictWine(self, wine: Wine):
        """
        Predict a wine based on Wine model instance.
        Use a random forest predictor saved in a joblib file.
        If there is no saved file, return an error message.
        """

        wine_dict = self.convertWineIntoDict(wine)
        if exists("./rfc.joblib"):
            random_forest = joblib.load("./rfc.joblib")
            del wine_dict["quality"]
            new_wine = json_normalize(wine_dict)
            pred_rfc = random_forest.predict(new_wine)
            return {"predict" : str(pred_rfc[0])}
        else:
            return {"error" : "No predictor loaded. Please retrain."}


    def retrain(self):
        """
        Retrain the model using all wines in the CSV file.
        Then save it in a joblib file.
        """

        data = pd.read_csv("./data/Wines.csv")
        del data['Id']
        X = data.drop('quality', axis=1)
        y = data['quality']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)
        random_forest = RandomForestClassifier(n_estimators=300)
        random_forest.fit(X_train, y_train)
        joblib.dump(random_forest, "./rfc.joblib")
        return {"message": "Successful retrain."}


    def addWine(self, wine: Wine):
        """ Add a Wine model instance in the CSV file. """

        wine_dict = self.convertWineIntoDict(wine)
        data = pd.read_csv("./data/Wines.csv")
        max_id = data['Id'].max()
        wine_dict['Id'] = max_id+1
        new_data = pd.DataFrame.from_dict([wine_dict])
        data = data.append(new_data, ignore_index=True)
        data.to_csv("./data/Wines.csv", index = False)
        return {"message": "Wine added in csv file."}


    def getPerfectWine(self):
        """ Return the best wine by sorting reversly the data and then take the first one. """

        data = pd.read_csv("./data/Wines.csv")
        data = data.sort_values(by=['quality'], ascending=False)
        wine_panda_object = data.iloc[0]
        return self.convertPandaObjectIntoWine(wine_panda_object)


    def getDescription(self):
        """ 
        Return all parameters from the random forest predictor, and the accuracy.
        If there is no saved file, return an error message.
        """

        if exists("./rfc.joblib"):
            random_forest = joblib.load("./rfc.joblib")
            data = pd.read_csv("./data/Wines.csv")
            del data['Id']
            X = data.drop('quality', axis=1)
            y = data['quality']
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)
            description = random_forest.get_params()
            description["accuracy"] = round(random_forest.score(X_test, y_test),3)
            return description
        else:
            return {"error" : "No predictor loaded. Please retrain."}
