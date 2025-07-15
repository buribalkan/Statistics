
import pandas as pd
import statsmodels.api as sm

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

X = sm.add_constant(x)
model = sm.OLS(y, X).fit()
print(model.summary())
