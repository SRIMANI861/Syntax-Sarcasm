lst = [10,15,20,25,30]
even_count = 0
odd_count = 0
for i in lst:
    if i%2 == 0:
        print(f"{i} is even")
        even_count += 1
    else:
        print(f"{i} is odd")
        odd_count += 1
print('Even numbers count: ', even_count)
print('Odd numbers count: ', odd_count)

