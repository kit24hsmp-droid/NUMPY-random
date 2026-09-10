from numpy import random 
x = random.normal(size = (2,3)) # Generate a 2-D array with 2 rows each row containing 3 random numbers from a normal distribution It generates random numbers around a mean (average).
print(x)

# random normal distribution of size 2 * 3 with mean 1 and standard deviation of 2
from numpy import random
x = random.normal(loc = 1, scale = 2, size = (2,3))
print(x)


#visualization of normal distribution using seaborn
from numpy import random 
import matplotlib.pyplot as plt
import seaborn as sns   
sns.displot(random.normal(size = 1000), kind = "kde") # Generate a random normal distribution of size 1000 and plot it using seaborn
plt.show()