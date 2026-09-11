from numpy import random 
import numpy as np 
arr = np.array([1, 2, 3, 4, 5]) # Create a numpy array
random.shuffle(arr) # Shuffle the array in place
print(arr) # Print the shuffled array


#generating permutation of an array 
from numpy import random 
import numpy as np 
arr = np.array([1,2,3,4,5]) # Create a numpy array
print(random.permutation(arr)) # Generate a random permutation of the array and print it