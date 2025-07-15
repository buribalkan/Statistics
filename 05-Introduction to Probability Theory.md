## 🎲 Introduction to Probability Theory



This section introduces the foundational concepts in probability — understanding uncertainty, randomness, and likelihood.



---



### ✅ Topics:



---



### 🎯 Sample Space, Events, and Outcomes



- **Outcome**: A single possible result of an experiment.  

  *Example:* Rolling a 4 on a die.



- **Sample Space (S)**: The set of all possible outcomes.  

  *Example:* For a six-sided die → S = {1, 2, 3, 4, 5, 6}



- **Event**: A subset of the sample space — one or more outcomes.  

  *Example:* Event A = rolling an even number = {2, 4, 6}



---



### ⚖️ Classical vs Empirical Probability



#### 🎓 Classical (Theoretical) Probability:

- Based on known possible outcomes, assuming they are **equally likely**.

- Formula:  

  **P(A) = Number of favorable outcomes / Total possible outcomes**



  *Example:* Probability of heads in a fair coin toss = 1/2



#### 📊 Empirical (Experimental) Probability:

- Based on actual **observations or experiments**.

- Formula:  

  **P(A) = Number of times event A occurs / Total trials**



  *Example:* If heads appears 47 times in 100 tosses,  

  → P(heads) ≈ 47 / 100 = 0.47



---



### ∪ ∩ ∁ Set Operations in Probability



#### 🔗 Union (A ∪ B)

- Event A **or** Event B occurs  

  *Example:* Rolling a number < 3 **or** an even number  

  - Includes {1, 2, 4, 6}



#### 🔗 Intersection (A ∩ B)

- Event A **and** Event B occur at the same time  

  *Example:* Rolling a number that is both < 3 **and** even → {2}



#### 🔁 Complement (Aᶜ or A')

- All outcomes **not** in event A  

  *Example:* If A = {1, 2, 3}, then Aᶜ = {4, 5, 6}



---



### 📌 Conditional Probability and Bayes' Theorem



#### 🔄 Conditional Probability:



> The probability of event A given that B has occurred.



- Notation: **P(A | B)**

- Formula:  

  **P(A | B) = P(A ∩ B) / P(B)**



*Example:*  

In a class of 10 students, 6 are girls, and 4 of them passed.  

If we pick a student and know she is a girl, what is the probability she passed?  

→ P(Passed | Girl) = 4 / 6



---



#### 🧠 Bayes' Theorem:



Used to reverse conditional probabilities.



- Formula:  

  **P(A | B) = [P(B | A) × P(A)] / P(B)**



Used in:

- Spam detection

- Medical diagnosis

- Machine learning classification



---



### 🔗 Independent vs Dependent Events



#### 🆓 Independent Events:

- One event does **not** affect the probability of the other.

  *Example:* Tossing two coins: result of one toss doesn’t affect the other.



  **P(A ∩ B) = P(A) × P(B)**



#### 🔗 Dependent Events:

- One event **does** affect the probability of the other.

  *Example:* Drawing cards without replacement.



---



## ✅ Summary Table



| Concept                | Description                                    | Example                         |

|------------------------|------------------------------------------------|---------------------------------|

| Sample Space           | All possible outcomes                         | Die roll: {1, 2, 3, 4, 5, 6}    |

| Classical Probability  | Based on theoretical assumptions              | Coin toss → 0.5                 |

| Empirical Probability  | Based on data/observations                   | 47 heads in 100 tosses → 0.47   |

| Union (A ∪ B)          | A or B (or both) happen                      | Rolling <3 or even → {1, 2, 4}  |

| Intersection (A ∩ B)   | A and B happen                                | Rolling <3 and even → {2}       |

| Complement (Aᶜ)        | What doesn’t belong to A                      | If A = {1,2}, Aᶜ = {3,4,5,6}    |

| Conditional P(A|B)     | A given B has happened                        | P(pass | girl) = 4 / 6          |

| Bayes’ Theorem         | Reverse conditional probability               | P(disease | positive test)      |

| Independent Events     | No influence                                  | Two coin tosses                 |

| Dependent Events       | One affects the other                         | Card draw without replacement   |



---



> 🧠 "Probability is orderly opinion."  

> — Bruno de Finetti
