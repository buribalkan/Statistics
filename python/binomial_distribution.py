import matplotlib.pyplot as plt
from scipy.stats import binom

n = 10
p = 0.5
x = range(0, n + 1)
probs = binom.pmf(x, n, p)

plt.bar(x, probs, color="skyblue")
plt.title("Binomial Distribution (n=10, p=0.5)")
plt.xlabel("Number of Successes")
plt.ylabel("Probability")
plt.grid(True)
plt.tight_layout()
plt.show()
