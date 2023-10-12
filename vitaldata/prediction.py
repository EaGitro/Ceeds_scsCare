import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris


class prediction:
    def __init__(self):
        self.date = 0
        self.heart_rate = 0
        self.blood_oxygen_concentration = 0
        self.average_sleep_time = 0

        self.productivity = 0

        self.clf = MLPClassifier(hidden_layer_sizes=(100,), max_iter=200)

    def train(self,X,y):
        self.clf.fit(X,y)

    def predict(self,X):
        pred = self.clf.predict(X)

        return pred
    
if __name__ == "__main__":
    iris = load_iris()
    train_X , target_X, train_y ,target_y = train_test_split(iris.data, iris.target)
    model = prediction()
    model.train(train_X,train_y)
    pred = model.predict(target_X)
    print(model.score(target_X,target_y))
