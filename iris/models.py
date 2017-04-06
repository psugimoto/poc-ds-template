# coding: utf-8
import pandas as pd
from sklearn.externals import joblib

from .train import Trainer

trainer = Trainer()
model = None
TARGETS = {
    0: 'Setosa',
    1: 'Versicolour',
    2: 'Virginica'
}


def load_model():
    global model, trainer
    try:
        model = joblib.load('model.pkl')
    except FileNotFoundError:
        return False

    trainer = Trainer(model)    # Stored global for later use
    return model


def predict(data):
    pd_data = pd.Series(data)
    return TARGETS[model.predict(pd_data)[0]]


def evaluate():
    global trainer
    try:
        return trainer.evaluate()
    except AttributeError:
        return None     # 'no model was trained yet'