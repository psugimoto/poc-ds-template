The app has 3 endpoints:
- /load - loads model.pkl into memory

- /evaluate - returns the precision of the model on a test dataset

- /predict - returns a prediction when the request contains a JSON with features. The prediction can be: Setosa, Versicolour or Virginica

            JSON example:
            {
                "sepal length": 5,
                "sepal width": 3,
                "petal length": 3,
                "petal width": 1,
            }
