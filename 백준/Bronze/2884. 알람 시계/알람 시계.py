a, b = map(int, input().split())
    
if b >= 45:
    b = b-45
else:
    a = a-1
    b = b+15

if a<0:
    a = 24+a

print(a,b)