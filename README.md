# TPWineQuality

## Installation 
python3.8 -m venv .venv

source .venv/bin/activate

After creating your environment, you have to install all necessary packages.

pip install -r requirements.txt

## Launch
python3 main.py

You have to execute python file.
To change the port, you can change the number in the file "main.py", at line 7.

To visualize all the endpoints and the API routes available, go to the following url :

http://localhost:8000/docs (replace 8000 by your port)

## Test
To execute the tests, write the following command line :

python3 -m pytest --cov

## Model construction

### Dataset

All data are stored in the file "Wines.csv"

They are used to train the model.

### Model

We used the scikit learn module "RandomForestClassifier" for the prediction.

All data are used in this model.

### Perfect wine

To find the perfect wine, we search for all wines that have the best quality in the dataset, and return one of them.

## Contributors
Thomas Bordis, bordisthom@cy-tech.fr

Florian Mounacq, mounacqflo@cy-tech.fr
