#Access and Traverse the list
shoppingList = ['Butter', 'Milk', 'Cheese']
print(shoppingList[0]) #Index access TC o(1)
print('Milk' in shoppingList) #in operator will check list if element is present

def traverse_list(shoppingList):
    for ele in shoppingList:
        print(ele)
traverse_list(shoppingList) #Tc o(n)

#Insert/Update the list
myList = [1, 2, 3, 4, 5, 6, 7]
myList[2] = 33 #Update the list by accessing the element TC o(1) Sc o(1)
print(myList) 

myList.insert(0, 11) #Inserting at the beginning of the list tc o(n)
print(myList)
myList.append(100) #Append the end of the list tc o(1)
print(myList)

newList = [13, 14, 15]
myList.extend(newList)
print(myList) #extent another list  tc: o(n)n is number of element in newList it loops and append

# Slice/Delete the list
myNewList = ['a', 'b', 'c', 'd', 'e', 'f']
print(myNewList[0:2])
myNewList.pop(1) #Will delete the index, if no index is provided then it will delete the last
# TC o(n), SC o(n)
print(myNewList)
del myNewList[2] #We can delete multiple element using slicing
# Tc o(n)
print(myNewList)
myNewList.remove('f') #Provide the element
#Tc o(n) 
print(myNewList)

#Searching for an element in the list
my_list = [10, 20, 30, 40, 50, 60, 70, 80]
if 20 in myNewList:
    print(f'{20} is in the list')

#Linear Search TC o(n) 
def linear_search(list, target):
    for i, value in enumerate(list):
        if value == target:
            return i
    return -1

print(linear_search(my_list, 20))

# List Operator and function
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b #Concatenate both the lisy
print(c)
d = [0]
print(4 * d)
print(len(c)) #give length of the list
print(max(c)) #return max
print(min(c))
print(sum(c)) 

# List and String
s1 = 'Span'
s1_list = list(s1)
print(s1_list)

s2 = 'span span span'
s2_list = s2.split()
print(s2_list)

s3 = 'span-span-span'
s3_list = s3.split('-')
print(s3_list)

# Keeping the original list
test = [1, 2, 3, 4, 5]
org = test[:]
org1 = test

test.append(10)
print(test)
print(org)
print(org1)
# see org1 is modified because refence is assigned rather than coping original lis
# In case of org the copy of the list is assigned

# List Comprehension
prev_list = [1, 2, 3]
new_list = [item*2 for item in prev_list]
print(new_list)
word = 'Aniket'
letters = [letter for letter in word]
print(letters)

# List Comprehension with Condition
# new_list = [item for item in old_list if condition]
p_list = [-1, 1, -2, 2, -3, 3]
n_list = [num for num in p_list if num > 0]
print(n_list)

def get_number(number):
    if number > 0:
        return number
    else:
        return 'Negative Number'
    
nn_list = [get_number(number) for number in p_list]

print(nn_list)

sentence = 'My Name is Aniket'
def is_consonent(sentence):
    vowel = 'aeiou'
    return [letter for letter in sentence if letter.lower() not in vowel and letter != ' ']

print(is_consonent(sentence))

