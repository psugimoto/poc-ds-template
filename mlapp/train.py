from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.externals import joblib


class Trainer:
    def __init__(self, model=None):
        iris = datasets.load_iris()

        data, labels = iris.data, iris.target
        self.data_train, self.data_test, self.labels_train, self.labels_test = train_test_split(data, labels,
                                                                                                test_size=0.2)
        self.model = model

    def train(self):
        self.model = KNeighborsClassifier(n_neighbors=3)
        self.model.fit(self.data_train, self.labels_train)

    def evaluate(self):
        return self.model.score(self.data_test, self.labels_test)

    def save(self):
        joblib.dump(self.model, 'model.pkl')