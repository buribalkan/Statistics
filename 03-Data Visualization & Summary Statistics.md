# 📊 Data Visualization & Summary Statistics

This section introduces common techniques for exploring and visualizing datasets, identifying outliers, and understanding the distribution of data.

---

## 📋 Frequency Tables

A **frequency table** displays how often each value (or range of values) appears in a dataset.


### Example:

| Score Range | Frequency |

|-------------|-----------|

| 0–10        | 3         |

| 11–20       | 5         |

| 21–30       | 7         |



Used for **categorical** or **discrete** data to identify distribution and patterns.



---



## 📉 Histograms

- **Purpose**: Show the distribution of a **continuous** variable.

- **How it works**: Groups data into **bins** and displays frequency per bin.

```python

import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv("your_data.csv")

plt.hist(df["height"], bins=10)

plt.title("Histogram of Height")

plt.xlabel("Height")

plt.ylabel("Frequency")

plt.show()

```
📦 Boxplots (Box-and-Whisker Plots)

Purpose: Visualize spread, median, and outliers.
Shows:
Median (line in the box)
Q1 (25th percentile) and Q3 (75th percentile)
Outliers as points
```python
import seaborn as sns
sns.boxplot(x=df["temperature"])
```

🔹 Scatterplots

Purpose: Show relationships between two numerical variables.
Ideal for detecting correlation or clusters.
```python

plt.scatter(df["hours_studied"], df["score"])

plt.xlabel("Hours Studied")

plt.ylabel("Score")

plt.title("Study Time vs Exam Score")

plt.show()
```

📊 Bar Charts

Used for categorical variables.
Displays frequency or proportion of each category.

```python
df["category"].value_counts().plot(kind="bar")
```
🥧 Pie Charts

Visualize proportions in a circular format.
Less effective than bar charts for comparison.

```python
df["category"].value_counts().plot(kind="pie", autopct="%1.1f%%")
```

📐 Skewness & Kurtosis

📏 Skewness:

Measures asymmetry of the distribution.
Positive skew: Tail on the right (e.g. income)
Negative skew: Tail on the left
```python
df["salary"].skew()
```
📎 Kurtosis:

Measures tailedness of distribution.
High kurtosis: Heavy tails (outliers)
Low kurtosis: Light tails
```python
df["salary"].kurt()
```
🚨 Outlier Detection

🔹 Z-score Method

Outlier if |z| > 3
```python
from scipy.stats import zscore

df["z_score"] = zscore(df["value"])

outliers = df[df["z_score"].abs() > 3]
```
🔸 IQR Method

Outlier if value is outside [Q1 - 1.5IQR, Q3 + 1.5IQR]
```python
Q1 = df["value"].quantile(0.25)

Q3 = df["value"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR

upper = Q3 + 1.5 * IQR

outliers = df[(df["value"] < lower) | (df["value"] > upper)]
```
📋 Summary Statistics with 

.describe()

Quick overview of central tendency and spread for each numerical column.
```python
df.describe()
```
Output includes:
count
mean
std
min, 25%, 50%, 75%, max



📌 Summary

Tool/Concept

Use Case

Frequency Table

Count of categorical values

Histogram

Distribution of continuous variable

Boxplot

Spread and outliers

Scatterplot

Relationship between two variables

Skewness & Kurtosis

Shape and tails of distribution

Z-score, IQR

Outlier detection

describe()

Fast numeric summary of data


---

> 🧠 “A picture is worth a thousand words — especially in data science.”

---
