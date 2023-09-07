n = int(input())
title = 1
count = 0

while True:
    if n == count:
        break
    title += 1
    
    string = str(title)
    
    if "666" in string:
        count += 1


print(title)    