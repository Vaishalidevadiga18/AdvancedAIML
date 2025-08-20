from sklearn.linear_model import LinearRegression
import numpy as np

# Training data
x = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# Fit model
model = LinearRegression()
model.fit(x, y)

# Prediction
print("Prediction for 6:", model.predict([[6]])[0])
