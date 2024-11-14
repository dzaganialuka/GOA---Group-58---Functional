number= int(input("enter number : "))
result = []
for num in range (1,number) :
    deviders = []
    for i in range [1,num +1]:
        if num %  i ==0 :
            deviders.append(i)
    if len(deviders)<=2:
        result.append(num)
