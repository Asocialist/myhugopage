# import numpy as np
# a = np.array([1, 2, 3])
# print(a)
# print(type(a))
# print(a.shape)
# print(a.dtype)

import numpy as np
student = np.dtype([('name','S20'),('age','i1'),('marks','f4')])
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student) 
print(a)