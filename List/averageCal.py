myList = []
while True:
    inp = input('Enter a number: ')
    if inp == 'done': break
    myList.append(float(inp))

print('Average:', sum(myList)/len(myList))