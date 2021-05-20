import sys
sys.setrecursionlimit(10000) 

n, m, k = map(int, input().split())
arr = [[0]*m for _ in range(n)]
for loc in range(k):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1


def dfs(x, y, size):
    px = [-1, 0, 0, 1]
    py = [0, -1, 1, 0]

    if x>=0 and x<n and y>=0 and y<m:
        if arr[x][y] == 1:
            size += 1
            arr[x][y] = 0
            for i in range(4):
                size = dfs(x+px[i], y+py[i], size)
    return size

result = 0
for i in range(n):
    for j in range(m):
        size = 0
        size = dfs(i, j, 0)
        result = max(result, size)

print(result)
