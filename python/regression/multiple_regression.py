
import pandas as pd
import statsmodels.api as sm

# Sample data
data = {
    'x1': [1, 2, 3, 4, 5],
    'x2': [2, 1, 4, 3, 5],
    'y':  [2, 3, 6, 5, 7]
}
df = pd.DataFrame(data)
X = df[['x1', 'x2']]
X = sm.add_constant(X)
y = df['y']

model = sm.OLS(y, X).fit()
print(model.summary())
