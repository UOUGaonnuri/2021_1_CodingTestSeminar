import sys

def binary_search(start, end, num):
    while start < end:
        mid = (end+start) // 2

        if result[mid] < num:
            start = mid + 1
        else:
            end = mid
    return end


n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
result = []

result.append(a[0])
for i in range(1, len(a)):
    if result[-1] < a[i]:
        result.append(a[i])
    else:
        index = binary_search(0, len(result)-1, a[i])
        result[index] = a[i]
        
        
print(len(result))
