n, k = map(int, input().split())
a=0
remain = k
arr = []
for i in range(n):
    arr.append(int(input()))

for i in range(n-1, -1, -1):
    a += remain // arr[i]
    remain = remain % arr[i]
    
    if remain == 0:
        break

print(a)