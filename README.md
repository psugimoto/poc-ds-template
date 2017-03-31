The app has 5 endpoints:
- /save  - persists the trained model (if it exists) in model.pkl

- /load - loads model.pkl into memory

- /train - trains a model using the Iris dataset from sklearn

- /evaluate - returns the precision of the model on a test dataset

- /predict - returns a prediction when the request contains a JSON with features. The prediction can be: Setosa, Versicolour or Virginica

            JSON example:
            {
                "sepal length": 5,
                "sepal width": 3,
                "petal length": 3,
                "petal width": 1,
            }
