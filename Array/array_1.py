# Array store Data of same data type
# Array Stored in contigous memory

#Creating an array TC: o(n) SC: o(n)

import array

my_array = array.array('i', [1, 2, 3, 4])
print(my_array)

import numpy as np

np_array = np.array([1, 2, 3, 4])
print(np_array)

#Inserting on array TC: o(n) shifting sc o(1)
my_array.insert(0, 6)
print(my_array)

#Array Traversal tc o(n) sc: o(1)
def traversal(array):
    for ele in array:
        print(ele)

traversal(my_array)

#Accessing Element TC: o(1), SC: o(1) Constant time operation
def accessElement(array, index):
    if index >= len(array):
        print('Invalid Index')
    else:
        return array[index]
print(accessElement(my_array, 4))

# Search for an element TC: o(n) SC: o(1)
def linear_search(array, ele):
    for i in range(len(array)):
        if array[i] == ele:
            return i
    return -1

print(linear_search(my_array, 3)) 

#Delete and element in array TC o(n), SC o(1)
arr1 = array.array('i', [1, 2, 3, 4, 5, 6])
arr1.remove(1)
print(arr1)









