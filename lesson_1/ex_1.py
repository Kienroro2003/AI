def countPositiveNumber(arr):
    count = 0
    for i in arr:
        if i > 0:   count += 1
    return count
def countNegativeNumber(arr):
    count = 0
    for i in arr:
        if i < 0:   count += 1
    return count
data1 = [-10, -21, -4, -45, -66, 93, 11, -4, -6, 12, 11, 4]
print(f"The number of negative number is: {countNegativeNumber(data1)}")
print(f"The number of positive number is: {countPositiveNumber(data1)}")