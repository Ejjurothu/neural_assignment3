import numpy as np
x = np.arange(1,21,dtype = float)
print("Vector :",x)
x=x.reshape(4,5)
print("Then reshape the array to 4 by 5:",x)
def replace(x):
    a=x
    a[:,np.argmax(x, axis=1)] = 0
    return a
result= replace(x)
print("replace the max in each row by 0 (axis=1):",result)