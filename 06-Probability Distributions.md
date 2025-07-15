## 📊 Stage 4: Probability Distributions



This section introduces **probability distributions** — mathematical functions that describe how probabilities are distributed over values of a random variable.



---



### ✅ Topics Covered:



---



## 🎲 Discrete Distributions



Used when the variable can take **countable values** (e.g. number of customers, number of successes).



---



### 🧮 Binomial Distribution



- Models the number of **successes** in a fixed number of independent Bernoulli trials.

- Each trial has two outcomes: success/failure.

- Parameters:  

  - **n**: number of trials  

  - **p**: probability of success



- Probability Mass Function (PMF):  

  **P(X = k) = C(n, k) × p^k × (1 - p)^(n - k)**



*Example:* Probability of getting 3 heads in 5 coin tosses.



```python

from scipy.stats import binom

binom.pmf(k=3, n=5, p=0.5)  # Output: 0.3125

```



---



🔢 Poisson Distribution


- Models the number of events occurring in a fixed interval of time/space.
- Used when events are rare and independent.
- Parameter:
- λ (lambda): expected number of occurrences
- PMF:

P(X = k) = (λ^k × e^(-λ)) / k!



Example: Number of customer arrivals per minute.

```python

from scipy.stats import poisson

poisson.pmf(k=4, mu=2)  # P(4 events when average is 2)

```



⸻



🎯 Geometric Distribution

	•	Models the number of trials until the first success.

	•	Memoryless property: previous failures don’t affect future outcome.

	•	Parameter:

	•	p: probability of success

	•	PMF:

P(X = k) = (1 - p)^(k - 1) × p



Example: Probability that first success is on the 4th trial.


```python
from scipy.stats import geom

geom.pmf(k=4, p=0.3)

```



⸻



📈 Continuous Distributions



Used when variables can take any value in a range (e.g. height, weight, time).



⸻



🧘‍♂️ Normal Distribution (Gaussian)

	•	Bell-shaped, symmetric around the mean.

	•	Parameters:

	•	μ (mu): mean

	•	σ (sigma): standard deviation

	•	PDF:

f(x) = (1 / √(2πσ²)) × e^(-(x - μ)² / (2σ²))



Example: Modeling test scores, heights, etc.

```python

from scipy.stats import norm

norm.pdf(x=170, loc=165, scale=10)  # Probability density at height = 170 cm
```




⸻



🎲 Uniform Distribution

	•	All values in a range are equally likely.

	•	Parameters:

	•	a: lower bound

	•	b: upper bound

	•	PDF:

f(x) = 1 / (b - a) for a ≤ x ≤ b



Example: Rolling a fair die (continuous approximation).


```python
from scipy.stats import uniform

uniform.pdf(x=3, loc=1, scale=6)  # Uniform over [1, 7)

```



⸻



⏳ Exponential Distribution

	•	Models the time between events in a Poisson process.

	•	Parameter:

	•	λ (rate parameter)

	•	PDF:

f(x) = λ × e^(-λx)



Example: Time between customer arrivals.


```python
from scipy.stats import expon

expon.pdf(x=2, scale=1/0.5)  # Mean = 1/λ = 2

```



⸻



📘 Central Limit Theorem (CLT)



The CLT states that the sampling distribution of the sample mean approaches a normal distribution as the sample size increases — regardless of the population’s original distribution.



	•	Conditions:

	•	Independent samples

	•	Sample size n ≥ 30 (rule of thumb)



Why it matters?

	•	Enables use of normal approximation for inference even when the original data is not normal.



⸻



📏 Standard Normal Distribution & Z-tables

	•	A special case of the normal distribution:

	•	Mean (μ) = 0

	•	Standard deviation (σ) = 1

	•	Z-score:

Z = (X - μ) / σ

	•	Z-tables give area (probability) under the curve to the left of a Z-value.



Example: What is the probability of a Z < 1.96?


```python
from scipy.stats import norm

norm.cdf(1.96)  # Output: ≈ 0.975
```




⸻



📌 Summary Table



Distribution	Type	Use Case Example

Binomial	Discrete	# of successes in fixed trials

Poisson	Discrete	Rare events per time/space unit

Geometric	Discrete	First success after trials

Normal	Continuous	Heights, IQ, test scores

Uniform	Continuous	Equal chance across a range

Exponential	Continuous	Time between arrivals

Standard Normal	Continuous	Z-scores and inference





⸻



🧠 “The normal distribution is not just a model — it’s the model behind many models.”

— Unknown



---
