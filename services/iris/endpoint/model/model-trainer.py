from sklearn import svm
from sklearn import datasets
from sklearn.externals import joblib

# SVMを訓練する
clf = svm.SVC()
iris = datasets.load_iris()
X, y = iris.data, iris.target
clf.fit(X, y)

# 予測結果を出力
print(clf.predict(X))

# 予測モデルをシリアライズ
joblib.dump(clf, 'clf.pkl') 