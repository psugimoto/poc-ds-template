import json
from app import app
from app import load_model
from flask_testing import TestCase

TEST_REQUEST = {
    "sepal length": 5,
    "sepal width": 3,
    "petal length": 3,
    "petal width": 1,
}


class Tests(TestCase):
    def setUp(self):
        load_model()

    def create_app(self):
        return app

    def make_request(self, endpoint, params=None):
        if params:
            return self.client.post(
                endpoint,
                data=json.dumps(params),
                content_type='application/json')
        else:
            return self.client.post(
                endpoint)

    def test_predict(self):
        response = self.make_request('/predict', TEST_REQUEST)
        self.assertEqual(response.status_code, 200)

    def test_predict_value(self):
        response = json.loads(self.make_request('/predict', TEST_REQUEST).data.decode('utf-8'))
        self.assertIn(response['predicted'], {'Virginica', 'Versicolour', 'Setosa'})

    def test_evaluate(self):
        response = self.make_request('/evaluate')
        self.assertEqual(response.status_code, 200)

    def test_evaluate_precision(self):
        response = json.loads(self.make_request('/evaluate').data.decode('utf-8'))
        self.assertTrue(response['precision'] > 0.5)
