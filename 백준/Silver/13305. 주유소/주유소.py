n = int(input())
a = 0
dist = list(map(int, input().split()))
price = list(map(int, input().split()))

min = price[0]

for i in range(n-1):
    if min > price[i]:
        min = price[i]
    a += min * dist[i]
    
print(a)