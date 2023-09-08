ans = 0
n = int(input())

arr = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    arr[i] = list(input())

def check(arr):
    max = 0
    sum = 0
    
    for i in range(n):
        if max < sum:
            max = sum
        sum = 0
        for j in range(n-1):
            if arr[i][j] == arr[i][j+1]:
                sum += 1
            else:
                if max < sum:
                    max = sum
                sum = 0
                
    for j in range(n):
        if max < sum:
            max = sum
        sum = 0
        for i in range(n-1):
            if arr[i][j] == arr[i+1][j]:
                sum += 1
            else:
                if max < sum:
                    max = sum
                sum = 0
    
    return max+1
    
    
def swap(arr, i, j):
    swapmax = 0
    
    if i > 0:
        arr[i-1][j], arr[i][j] = arr[i][j], arr[i-1][j]
        temp = check(arr)
        if temp > swapmax:
            swapmax = temp
        arr[i-1][j], arr[i][j] = arr[i][j], arr[i-1][j]
    
    if i < n-1:
        arr[i+1][j], arr[i][j] = arr[i][j], arr[i+1][j]
        temp = check(arr)
        if temp > swapmax:
            swapmax = temp
        arr[i+1][j], arr[i][j] = arr[i][j], arr[i+1][j]
        
    if j > 0:
        arr[i][j-1], arr[i][j] = arr[i][j], arr[i][j-1]
        temp = check(arr)
        if temp > swapmax:
            swapmax = temp
        arr[i][j-1], arr[i][j] = arr[i][j], arr[i][j-1]
   
    if j < n-1:
        arr[i][j+1], arr[i][j] = arr[i][j], arr[i][j+1]
        temp = check(arr)
        if temp > swapmax:
            swapmax = temp
        arr[i][j+1], arr[i][j] = arr[i][j], arr[i][j+1]
        
    return swapmax
  
for i in range(n):
    for j in range(n):
        swapmax = swap(arr, i, j)
        if ans < swapmax:
            ans = swapmax

print(ans)