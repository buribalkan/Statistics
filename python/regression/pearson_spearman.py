
import pandas as pd
from scipy.stats import pearsonr, spearmanr

# Sample data
x = [10, 20, 30, 40, 50]
y = [12, 24, 33, 45, 55]

pearson_corr, _ = pearsonr(x, y)
spearman_corr, _ = spearmanr(x, y)

print("Pearson Correlation:", pearson_corr)
print("Spearman Correlation:", spearman_corr)
