a = int(input("give me a number:"))

for i in range(1, a//2+1):
    if not a%i:
        print(i)