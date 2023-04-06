a, b, c = map(int, input().split())

if a == b and b == c and c == a:
    total = 10000+(a*1000)
elif a != b and b != c and c != a:
    total = max(a, b, c)*100
else:
    if a == b:
        total = 1000+(a*100)
    elif b == c:
        total = 1000+(b*100)
    else:
        total = 1000+(a*100)

print(total)