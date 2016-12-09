import numpy as np

# arr1 = np.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]], dtype=np.float)
# print(arr1.reshape(12, 2))
# print(arr1)
# arr1[2][2]=9
# print(arr1.reshape(12, 2))
# print(arr1)
# print(set(np.typeDict.values()))
# arr2=np.logspace(0,1,1000,base=2,endpoint=False)
# print(arr2)
# arr3 = np.empty()
# print(arr3)
# str='Hello World'
# str_arr=np.fromstring(str,dtype=np.int8)
# print(str_arr)
# def func(i, j):
# 	return (i + 1) * (j + 1)
#
#
# arr4 = np.fromfunction(func, (9, 9))
# print(arr4)
# tj = arr4 > 50
# print(tj)
# print(len(arr4[tj]))
# print(arr4[tj].reshape(5,2))
# print(arr4[3:7,[1,3,5,7]])
# print(arr4[[1, 2]])
# personType = np.dtype({
# 	'names'  : ['name', 'age'],
# 	'formats': ['S32', 'i']
# }, align=True)
# print(personType)
# a = np.array([('wxj', 20), ('cy', 19)], dtype=personType)
# print(a)
# print(a.dtype)
# print(a['name'][0])
# print(a[0][0].dtype)
# a.tofile('a.txt')
# a = np.fromfile('a.txt', dtype=personType)
# print(a.dtype)
# a = np.linspace(0, 10, 10, endpoint=False)
# b = np.linspace(0, 20, 10, endpoint=False)
# print(a <= b)
# a = np.arange(0, 60, 10).reshape(6, 1)
# print(a)
# b = a.repeat(5, axis=1)
# print(b)
arr5 = np.random.randint(0, 10, size=(100, 100))
print(np.argmax(arr5))
