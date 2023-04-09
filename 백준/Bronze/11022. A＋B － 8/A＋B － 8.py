t = int(input())

for i in range(0, t):
    a, b = map(int, input().split())
    print("Case #", i+1, ": ", a, " + ", b, " = ", a+b, sep='')