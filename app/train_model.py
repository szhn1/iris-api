from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from joblib import dump

# Загрузка данных
iris = load_iris()
X, y = iris.data, iris.target

# Обучение модели
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

# Сохранение модели
dump(model, 'app/iris_model.joblib')
print("Model saved!")