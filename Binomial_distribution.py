#binomial distribution is a discrete probability distribution that describes the number of successes in a fixed number of independent Bernoulli trials, each with the same probability of success. It is used to model situations where there are two possible outcomes (success or failure) and we want to know the probability of a certain number of successes in a given number of trials.  
from numpy import random
# Generate a random number from a binomial distribution with n=10 trials and p=0.5 probability of success and 10 data 
x = random.binomial(n=10, p=0.5, size = 10)
print(x)

# visualization of binomial distribution using seaborn
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(random.binomial(n=10, p=0.5, size = 1000)) # Generate a random binomial distribution of size 1000 and plot it using seaborn
plt.show()

# Difference Between Normal and Binomial Distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

data = {
  "normal": random.normal(loc=50, scale=5, size=1000),
  "binomial": random.binomial(n=100, p=0.5, size=1000)
}

sns.displot(data, kind="kde")

plt.show()
