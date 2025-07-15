
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 5, 4, 5])

model = LinearRegression().fit(x, y)
predictions = model.predict(x)
residuals = y - predictions

print("R²:", r2_score(y, predictions))

plt.scatter(x, y, label="Actual")
plt.plot(x, predictions, color="red", label="Predicted")
plt.legend()
plt.title("Residuals & R²")
plt.show()
