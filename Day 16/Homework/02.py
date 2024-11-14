input_set = {1, 2, 3, 4, 5}
for item in input_set:
    fact = 1
    for number in range(1,item+1):
        fact = fact * number
        print ("Factorial of", input, "is", fact)