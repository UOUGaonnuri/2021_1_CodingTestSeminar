import sys
from bisect import bisect_left
N = sys.stdin.readline().rstrip()

array = list(map(int, sys.stdin.readline().split()))

result = []

for i in array:
    k = bisect_left(result, i)
    if len(result) <= k:
        result.append(i)
    else:
        result[k] = i

print(len(result))
