#ფაქტორიალი არის ფაქტორიალი არის ყველა მთელი რიცხვის გამრავლების ჯამი, ჩვენი მითითებული რიცხვიდან 1-მდე. მაგალითად, 6-ის ფაქტორიალი იქნება 6 x 5 x 4 x 3 x 2 x 1 = 720
num = int(input("enter num: "))
fact = 1
for i in range(1, num+1):
    fact = fact * i
print("The factorial of num is : ", end="")
print(fact)