import os
import pickle



from flask import Flask
from flask import jsonify

import numpy as np
import pandas as pd
import sklearn
from sklearn.metrics import mean_absolute_error, mean_squared_error
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__






def load_data() :
   
    df = pd.read_csv("data/processed/housing_test.csv")
    y = df["median_house_value"].copy(deep=True)
    X = df.drop(["median_house_value"], axis=1)
    return (X, y)



def score_model(model, X,y, args) :
 
    scores = {}
    scores["R2 score"] = model.score(X, y)
    y_hat = model.predict(X)

    if args.rmse:
        rmse = np.sqrt(mean_squared_error(y, y_hat))
        scores["RMSE"] = rmse

    if args.mae:
        mae = mean_absolute_error(y, y_hat)
        scores["MAE"] = mae

    return scores


def get_weights_blob():
    connection_string = 'DefaultEndpointsProtocol=https;AccountName=storageaccount4123;AccountKey=U3cht849LFhus3wEcd+3GufqatKR2eijd0rB9gV58oCLXYe6rjMy15J/sk4ZYkSeoGU5X864awQ/+AStkA8T8A==;EndpointSuffix=core.windows.net'
    
    blob_client = BlobClient.from_connection_string(connection_string, container_name="data", blob_name ="RandomForestRegressor.pkl" )
    downloader = blob_client.download_blob(0)

    # Load to pickle
    b = downloader.readall()
    weights = pickle.loads(b)

    return weights




X, y = load_data()


model = get_weights_blob()

print(model)

app = Flask(__name__)
@app.route('/')
def hello_world():
    return "flask_app"

@app.route('/predict', methods=["POST", "GET"])
def predict():
    scores = {}
    
         
    scores["R2 score"] = model.score(X, y)
    y_hat = model.predict(X)

        
    rmse = np.sqrt(mean_squared_error(y, y_hat))
    scores["RMSE"] = rmse

        
    mae = mean_absolute_error(y, y_hat)
    scores["MAE"] = mae

        

    return jsonify(scores)
       


app.run(host ='0.0.0.0', port = 5000, debug = True) 


