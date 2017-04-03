import pandas as pd
from flask import Flask, request
from flask.json import jsonify
from train import Trainer
from sklearn.externals import joblib

app = Flask(__name__)

trainer = Trainer()
model = None
TARGETS = {0: 'Setosa',
           1: 'Versicolour',
           2: 'Virginica'}


def save_model():
    global trainer
    if trainer.model is None:
        trainer.train()
    trainer.save()
    return 'Model saved', 200


@app.route('/load', methods=['POST', 'GET'])
def load_model():
    global model, trainer
    try:
        model = joblib.load('model.pkl')
        if trainer.model is None:
            trainer = Trainer(model)
        return 'Model loaded', 200
    except FileNotFoundError:
        return 'Model does not exist', 500


def train():
    global trainer
    trainer.train()
    return 'Model trained', 200


@app.route('/evaluate', methods=['POST', 'GET'])
def evaluate():
    global trainer
    try:
        return jsonify(**{'precision': trainer.evaluate()}), 200
    except AttributeError:
        return 'Model is empty', 500


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    data = pd.Series(request.get_json())
    if model is None:
        load_model()
    return jsonify(predicted=TARGETS[model.predict(data)[0]]), 200

if __name__ == "__main__":
    load_model()
    trainer = Trainer(model)
    app.run()

