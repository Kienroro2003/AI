data3 = [4, 5, 6, 7, 3, 9, 11, 2, 10]
max = data3[0]

for i in data3:
    if max < i: max = i

print(f"The maximum value in the dataset is: {max}")