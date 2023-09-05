from operator import itemgetter

n = int(input())

arr = []
group = []

count = 0
end = 0

for i in range(n):
    a, b = map(int, input().split())
    arr.append(a)
    arr.append(b)
    
for i in range(0, len(arr), 2):
    group.append(arr[i:i+2])
    
sorted_group = sorted(group, key=lambda x: (x[1], x[0]))



for i in range(n):
    if i == 0:
        count+=1
        end = sorted_group[i][1]
    else:
        if sorted_group[i][0] < end:
            continue
        else:
            count+=1
            end = sorted_group[i][1]

print(count)