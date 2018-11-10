"""test batch script"""
from sklearn import datasets
from lib.state import iris_service

iris = iris_service.IrisStateService()

# データセットを再読み込み
iris_datasets = datasets.load_iris()

for i, data in enumerate(iris_datasets.data):
    iris.update(i, data.tolist())
