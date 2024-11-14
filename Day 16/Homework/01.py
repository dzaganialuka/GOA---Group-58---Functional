my_list = [2, 3, 5, 6, 7, 8, 9]
largest_str = my_list[0]
for i in my_list:
    if i > largest_str:
        largest_str = i

print("largest_str:", largest_str)