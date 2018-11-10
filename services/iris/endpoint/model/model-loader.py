from sklearn import datasets
from sklearn.externals import joblib

# データセットを再読み込み
iris = datasets.load_iris()

# 予測モデルを復元
clf = joblib.load('clf.pkl') 

print(iris.data)

# 予測結果を出力
print(clf.predict(iris.data))