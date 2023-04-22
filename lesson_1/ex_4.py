def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

data4 = [1, 2, 3]

n = len(data4) - 1

i = -2

while(i != -1):
    print(f"{data4[0]} {data4[1]} {data4[2]}")
    i = n - 1
    while i > -1 and data4[i] > data4[i + 1] : i -= 1
    if i > -1:
        k = n
        while data4[k] < data4[i]: k -= 1
        swap(data4, i, k)
        a = i + 1
        b = n
        while a < b:
            swap(data4, a , b)
            a += 1
            b -= 1

