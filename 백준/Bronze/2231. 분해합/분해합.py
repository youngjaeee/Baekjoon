n = int(input())
partialSum = 0

for i in range(0, n):
    if(i == n-1):
        print("0")
        break
    
    partialSum = i
    k = i
    while i > 0:
        partialSum += i % 10
        i = i//10
        
    if partialSum == n:
        print(k)
        break