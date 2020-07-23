import numpy as np 
import pandas as pd
from numpy.random import randn


labels = ['a', 'b','c']
my_data = [10,20,30]

arr = np.array(my_data)

d = { 'a':10, 'b':20, 'c':30}


#series
s = pd.Series(data=my_data,index=labels)
#print(s)


#np.random.seed(101)

df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df.W)