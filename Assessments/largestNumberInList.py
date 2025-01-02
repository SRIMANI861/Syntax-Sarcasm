lst = [5,3,8,2,10]

largest = lst[0]
for i in lst:
    if i > largest:
        largest = i
print('Largest Number is: ', largest)