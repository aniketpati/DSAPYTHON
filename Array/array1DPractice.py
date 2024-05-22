from array import *

#Creating and Traversal of array
my_array = array('i', [1, 2, 3, 4, 5])
def array_traversal(arr):
    for i in my_array:
        print(i)

array_traversal(my_array)
print('------------')

# Access element with index
print(my_array[0])
print('------------')

# Insert any value with append method
my_array.append(6)
print(my_array) 
print('------------')

# Insert value in a array using insert method
my_array.insert(1, 10)
print(my_array)
print('------------')

# Extend python array using extent() method
my_array.extend(array('i', [12, 13, 14]))
print(my_array)
print('------------')

# Add items from list into array using fromList() method
tempList = [20, 21, 22]
my_array.fromlist(tempList)
print(my_array)
print('------------')

# Remove element from array
my_array.remove(20)
print(my_array)
print('------------')

# Remove last element from Array
my_array.pop()
print(my_array)
print('------------')

# Fetch any element through its index() method
print(my_array.index(21))
print('------------')

# Reverse a python array using reverse()
my_array.reverse()
print(my_array)
print('------------')

# Get array buffer information through buffer_info() method
print(my_array.buffer_info())
print('------------')

# Number of occurence of element using count
print(my_array.count(1))
print('------------')

# Covert Array to List
# print(my_array.tolist())
print('------------')

# Slice elements from an array
print(my_array[1:4])












