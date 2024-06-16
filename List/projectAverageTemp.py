inp = input('How many days temperature? ')
noofDays = int(inp)
day = 1
tempList = []
while noofDays >= day:
    temp = input(f'Day {day} highest temp? ')
    tempList.append(int(temp))
    day = day + 1
avg = sum(tempList)/len(tempList)
print(f'Average = {avg}')

tempList2 = [ele for ele in tempList if ele > avg]
print(f'{len(tempList2)} days above average temp')