sum = 0
numbers = range(1,21,1)
for number in numbers:
    if number % 2 == 1:
        sum += number
print(sum)