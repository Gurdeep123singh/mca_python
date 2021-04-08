
import numpy as np

x=np.arange(5)
print(x)
print(x[x<3])
print(x>3)
x[x>3]=100   # means those elements which are greater than 3 makes 100
print(x)

'''
o/p :-
[0 1 2 3 4]   size 5 ascending order
[0 1 2]          less than 3  if x is not there in 7th line [true true true False  false] means x<3
[False False False False  True]    means x>3
[  0   1   2   3 100]             
'''