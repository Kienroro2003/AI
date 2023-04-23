start = 2000
end = 3200
count = 0
while(start <= end):
    if (start % 5 == 0):
        start += 1
        continue
    if(start % 7 == 0):
        print(start, end=', ')
    start += 1