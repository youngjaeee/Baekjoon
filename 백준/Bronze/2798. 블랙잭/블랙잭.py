n, m = map(int, input().split())
arr = list(map(int, input().split()))
max = 0
arr.sort()

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum = arr[i] + arr[j] + arr[k]
            if sum > m:
                break
            if sum > max and sum <= m:
                max = sum

print(max)