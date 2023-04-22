data2 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k = int(input("Enter a your number: "))

filter_data = [x for x in data2 if x > k]
print(filter_data)