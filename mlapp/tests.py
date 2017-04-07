# coding: utf-8
from __future__ import unicode_literals

from django.test import TestCase

from .management.commands import train

import pytest


def test_dumb():
    assert 1+1 == 2


class TestIndex(TestCase):
    def setUp(self):
        train.Command().handle()
        self.client.post('/load')

    def test_load_model(self):
        # 0: Endpoints list
        response = self.client.post('/load')
        assert response.status_code == 200

    def test_evalueate_model(self):
        response = self.client.get('/evaluate')
        assert response.status_code == 200
        assert 'precision' in response.json()

    def test_predict(self):
        response = self.client.post('/predict', {
            "sepal length": 5,
            "sepal width": 3,
            "petal length": 3,
            "petal width": 1,
        })
        assert response.status_code == 200
        assert 'predicted' in response.json()
        assert response.json()['predicted'] in {'Virginica', 'Versicolour', 'Setosa'}