import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

x = np.linspace(-4, 4, 1000)
y = norm.pdf(x, loc=0, scale=1)

plt.plot(x, y, color="green")
plt.title("Standard Normal Distribution")
plt.xlabel("x")
plt.ylabel("Density")
plt.grid(True)
plt.tight_layout()
plt.show()
