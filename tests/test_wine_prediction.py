from wine_prediction import WinePrediction
import unittest

from models.wine import Wine

wine_prediction = WinePrediction()

class TestWinePrediction(unittest.TestCase):
    wine = Wine(
        fixed_acidity = 2, 
        volatile_acidity = 3,
        citric_acid = 4,
        residual_sugar = 5,
        chlorides = 6,
        free_sulfur_dioxide = 7,
        total_sulfur_dioxide = 6,
        density = 5,
        pH = 4,
        sulphates = 3,
        alcohol = 2,
        quality = 1
    )

    def testConvertWineIntoDict(self):
        expected_wine_dict = {
            "fixed acidity": 2,
            "volatile acidity": 3,
            "citric acid": 4,
            "residual sugar": 5,
            "chlorides": 6,
            "free sulfur dioxide": 7,
            "total sulfur dioxide": 6,
            "density": 5,
            "pH": 4,
            "sulphates": 3,
            "alcohol": 2,
            "quality": 1
        }
        wine_dict = wine_prediction.convertWineIntoDict(self.wine)
        self.assertEqual(wine_dict, expected_wine_dict)


    def testPredictWine(self):
        expected_predict = {"predict": '1.0'}
        predict = wine_prediction.predictWine(self.wine)
        self.assertEqual(predict, expected_predict)


    def testRetrain(self):
        expected_retrain = {"message": "Successful retrain."}
        retrain = wine_prediction.retrain()
        self.assertEqual(retrain, expected_retrain)


    def testAddWine(self):
        expected_add = {"message": "Wine added in csv file."}
        add = wine_prediction.addWine(self.wine)
        self.assertEqual(add, expected_add)


    def testGetPerfectWine(self):
        expected_perfect_wine = Wine(        
            fixed_acidity = 10, 
            volatile_acidity = 10,
            citric_acid = 10,
            residual_sugar = 10,
            chlorides = 10,
            free_sulfur_dioxide = 10,
            total_sulfur_dioxide = 10,
            density = 10,
            pH = 10,
            sulphates = 10,
            alcohol = 10,
            quality = 10
        )
        perfect_wine = wine_prediction.getPerfectWine()
        self.assertEqual(perfect_wine, expected_perfect_wine)


    def testGetDescription(self):
        expected_description = "Ma description"
        description = wine_prediction.getDescription()
        self.assertEqual(description, expected_description)