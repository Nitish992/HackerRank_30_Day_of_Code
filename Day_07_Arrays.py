#!/bin/python3
n = int(input())

arr = list(map(str, input().rstrip().split()))
start = 0
end = len(arr)-1
while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -=1
for num in arr:
    print(num + " ", end="")
        
        