n = int(input())
a = 0

arr = list(map(int, input().split()))

arr.sort()

for i in range(n):
    a += arr[i]*(n-i)
    
print(a)