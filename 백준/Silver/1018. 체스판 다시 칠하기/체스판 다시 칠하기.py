row, col = map(int, input().split())
min = 2500
w_count = 0
b_count = 0

arr = [[0 for j in range(col)] for i in range(row)]

for i in range(row):
    str = input()
    arr[i] = list(str)
  
    
for i in range(row-7):
    for j in range(col-7):
        for k in range(8):
            for l in range(8):
                if (k+l)%2 == 0:
                    if arr[i+k][j+l] == 'B':
                        w_count += 1
                else:
                    if arr[i+k][j+l] == 'W':
                        w_count += 1
        
        if min > w_count:
            min = w_count
        w_count = 0
        
for i in range(row-7):
    for j in range(col-7):
        for k in range(8):
            for l in range(8):
                if (k+l)%2 == 0:
                    if arr[i+k][j+l] == 'W':
                        b_count += 1
                else:
                    if arr[i+k][j+l] == 'B':
                        b_count += 1
        
        if min > b_count:
            min = b_count
            
        b_count = 0
    
print(min)