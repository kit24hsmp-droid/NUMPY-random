# generate a random integer from 0 to 100
from numpy import random
x = random.randint(100) # Generate a random integer from 0 to 100
print(x)


# generate a random float from 0 to 1
from numpy import random
x = random.rand() # Generate a random float from 0 to 1
print(x)

#generata a random array 1d array of 5 elements this is used to generate a random 1D array of 5 elements    
from numpy import random
x = random.randint(100, size=(5)) # Generate a random 1D array of 5 elements
print(x)


# Generate a random 2-D array with 3 rows each row containing 5 random integers from 0 to 100
from numpy import random 
x = random.randint(100, size=(3,5)) # Generate a random 2-D array with 3 rows each row containing 5 random integers from 0 to 100
print(x)


#generate a 1d array containing 5 random floats
from numpy import random 
x = random.rand(5) # Generate a 1D array containing 5 random floats
print(x)

#generate a 2d array with 3 rows each rows containing 5 random numbers
from numpy import random 
x = random.rand(3,5) # Generate a 2D array with 3 rows each row containing 5 random numbers
print(x)