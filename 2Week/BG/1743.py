import sys
sys.setrecursionlimit(100000)

n, m, k = map(int, sys.stdin.readline().split())

waste = [[0 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())
    waste[r-1][c-1] = 1

check = [[False for _ in range(m)] for _ in range(n)]


def dfs(x, y):
    global cnt
    check[x][y] = True
    if waste[x][y] == 1:
        cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if waste[nx][ny] == 1 and not check[nx][ny]:
                dfs(nx, ny)


result = 0
for i in range(n):
    for j in range(m):
        if waste[i][j] == 1 and not check[i][j]:
            cnt = 0
            dfs(i, j)
            result = max(result, cnt)

print(result)
