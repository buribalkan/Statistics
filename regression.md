---
layout: default
title: Regression & Correlation
---

## 📉 Stage 6: Regression & Correlation

Understanding how two or more variables relate to each other is fundamental in statistics. Regression and correlation help us explore, model, and predict these relationships.

---

### 📌 Correlation Coefficient

Correlation measures the **strength and direction** of a relationship between two variables.

#### 🔹 Pearson Correlation
- Measures **linear** correlation.
- Ranges from **-1** (perfect negative) to **+1** (perfect positive).
- **0** indicates no linear correlation.

> Example: The correlation between height and weight.

#### 🔹 Spearman Correlation
- Measures **monotonic** relationships.
- Based on **rankings** of the data.
- Useful when the data is not normally distributed or not linear.

> Example: Correlation between exam rank and study hours.

📥 [Download pearson_spearman.py](python/regression/pearson_spearman.py)

---

### 📈 Simple Linear Regression

A model to describe the **linear relationship** between two variables:

\[
y = \beta_0 + \beta_1 x + \varepsilon
\]


import pandas as pd
import statsmodels.api as sm

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

X = sm.add_constant(x)
model = sm.OLS(y, X).fit()
print(model.summary())





📥 [Download simple_regression.py](python/regression/simple_regression.py)

---

### 🧮 Multiple Linear Regression

Extends simple regression to **multiple predictors**:

\[
y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + ... + \beta_n x_n + \varepsilon
\]

📥 [Download multiple_regression.py](python/regression/multiple_regression.py)

---

### 📊 Residuals & R²

Residuals are the **differences between predicted and actual values**.  
**R²** shows the **proportion of variance** in the dependent variable explained by the model.

📥 [Download residuals_r2.py](python/regression/residuals_r2.py)

---

### 🔄 Logistic Regression

Used when the **dependent variable is categorical**, especially binary (yes/no, 0/1):

\[
P(y=1) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 x)}}
\]

📥 [Download logistic_regression.py](python/regression/logistic_regression.py)
