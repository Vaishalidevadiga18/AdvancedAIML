
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
iris = load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
k = 5
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print("Prediction Results:\n")
for i in range(len(y_test)):
 actual = target_names[y_test[i]]
 predicted = target_names[y_pred[i]]
 if y_test[i] == y_pred[i]:
    print(f"Correct: Predicted = {predicted}, Actual = {actual}")
 else:
    print(f"Wrong: Predicted = {predicted}, Actual = {actual}")