def thisFunction(mylist=[], *myNum):
    print(mylist)
    print(*myNum)

    for x in list(int(mylist)):
        if x > myNum:
            mylist.remove(x)
            mylist.sort()
        elif x < myNum:
             print(f"There are no values less than numbers{myNum}")

thisFunction()