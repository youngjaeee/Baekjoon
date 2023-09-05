n = int(input())
a = 0

dist = list(map(int, input().split()))
price = list(map(int, input().split()))

price.pop()
n -= 1

while True:
    if len(price) == 0:
        break
    cheap = price.index(min(price))
    for i in range(cheap, n):
        a += price[cheap]*dist[i]
        
    for i in range(cheap, n):
        del dist[cheap]
        del price[cheap]
        
    n = cheap
    
print(a)