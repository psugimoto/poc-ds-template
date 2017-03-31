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

request_example = {
    "sepal length": 5,
    "sepal width": 3,
    "petal length": 3,
    "petal width": 1,
}


@app.route('/save')
def save_model():
    global trainer
    if trainer.model is not None:
        trainer.save()
    else:
        raise AttributeError('Model is empty')
    return 'Model saved'


@app.route('/load')
def load_model():
    global model
    try:
        model = joblib.load('model.pkl')
    except FileNotFoundError:
        print('Model is empty, training one from scratch')
        trainer.train()
        model = trainer.model
    return 'Model loaded'


@app.route('/train')
def train():
    global trainer
    trainer.train()
    return 'Model trained'


@app.route('/evaluate')
def evaluate():
    global trainer
    return trainer.evaluate()


@app.route('/predict')
def predict():
    data = pd.Series(request.get_json())
    return jsonify(predicted=TARGETS[model.predict(data)[0]])

if __name__ == "__main__":
    app.run()

