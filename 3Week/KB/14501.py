import sys

n = int(sys.stdin.readline())
d =[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = [0] * n
result.append(0)

for i in range(n-1, -1, -1):
    if i + d[i][0] > n:
        result[i] = result[i+1]
    else:
        result[i] = max(result[i+d[i][0]] + d[i][1], result[i+1])

print(result[0])
