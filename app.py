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
    return 'Model saved'


@app.route('/load')
def load_model():
    global model
    try:
        model = joblib.load('model.pkl')
    except FileNotFoundError:
        return 'Model does not exist'
    return 'Model loaded'


def train():
    global trainer
    trainer.train()
    return 'Model trained'


@app.route('/evaluate')
def evaluate():
    global trainer
    try:
        return trainer.evaluate()
    except AttributeError:
        return 'Model is empty'


@app.route('/predict')
def predict():
    data = pd.Series(request.get_json())
    if model is None:
        load_model()
    return jsonify(predicted=TARGETS[model.predict(data)[0]])

if __name__ == "__main__":
    train()
    load_model()
    app.run()

