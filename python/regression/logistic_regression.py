
import pandas as pd
from sklearn.linear_model import LogisticRegression

# Sample data
df = pd.DataFrame({
    'age': [22, 25, 47, 52, 46, 56],
    'bought': [0, 0, 1, 1, 1, 1]
})

X = df[['age']]
y = df['bought']

model = LogisticRegression()
model.fit(X, y)

age = [[30]]
prediction = model.predict_proba(age)
print(f"Probability of buying at age 30: {prediction[0][1]:.2f}")
