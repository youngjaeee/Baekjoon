n = int(input())
ans = -1


k = n//5

for i in range(k+1):
    remain = n - 5 * i
    if remain % 3 == 0:
        ans = i + remain / 3

print(int(ans))