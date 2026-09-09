from numpy import random 
x = random.choice([3,5,7,9], p = [0.1,0.3,0.6,0.0], size = (100)) # Generate a random number from the given list with specified probabilities
print(x)


# 2- D array with 3 rows each row containing 5 random numbers from the given list with specified probabilities
from numpy import random 
x = random.choice([3,5,7,9], p = [0.1,0.3,0.6,0.0], size = (3,5)) # Generate a 2-D array with 3 rows each row containing 5 random numbers from the given list with specified probabilities
print(x)