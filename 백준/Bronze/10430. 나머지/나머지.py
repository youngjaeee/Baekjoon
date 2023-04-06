key1, key2, key3 = input().split()

A = int(key1)
B = int(key2)
C = int(key3)

print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)