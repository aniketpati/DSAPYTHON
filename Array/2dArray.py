import numpy as np

twoDArray = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(twoDArray)

# Insert Element in 2D Array
# We cannot insert single element, we have to insert row or column TC: o(mn)
newTwoDArray = np.insert(twoDArray, 0, [[10, 11, 12, 13]], axis=0)
print(newTwoDArray)
# Insertion axis=0 Row, axis=1 Column

#append
newTwoDArray = np.append(twoDArray, [[100, 200, 300, 400]], axis=0)
print(newTwoDArray)

# Accessing elements in 2d array
# array[rowIndex][columnIndex]
# Access 100
def access_element(array, rowIndex, columnIndex):
    if rowIndex >= len(array) and columnIndex >= len(array[0]):
        print('Incorrect Index')
    else:
        print(array[rowIndex][columnIndex])

access_element(newTwoDArray, 3, 0)

# Travesal in 2D Array TC: 0(mn) SC: o(1)
def array_traversal(array):
    for rowIndex in range(len(array)):
        for columnIndex in range(len(array[rowIndex])):
            print(array[rowIndex][columnIndex])

array_traversal(newTwoDArray)

# Linear search in 2D Array TC o(mn) SC O(1)
def linear_search(array, target):
    for rowIndex in range(len(array)):
        for columnIndex in range(len(array[rowIndex])):
            if target == array[rowIndex][columnIndex]:
                print(f'Found at index {rowIndex}, {columnIndex}')
                return
    print('Not Found')

linear_search(newTwoDArray, 100)

# Deletion of row or column of 2d Array TC: o(mn) SC: o(mn) Axis=0(row) Axis=1 (Column)
newDeleteArray = np.delete(newTwoDArray, 0, axis=0)
print(newDeleteArray)
    