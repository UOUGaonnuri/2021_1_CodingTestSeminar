import sys
import copy
sys.setrecursionlimit(10000)

N = int(sys.stdin.readline())
area = [list(map(int, input.split())) for _ in range(N)]
result = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, h):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if(0 <= nx < N) and (0 <= ny < N):
            if area[nx][ny] > h and done[nx][ny] == 0:
                done[nx][ny] = 1
                dfs(nx, ny, h)


for k in range(max(map(max, area))):
    cnt = 0
    done = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if area[i][j] > k and done[i][j] == 0:
                done[i][j] = 1
                cnt += 1
                dfs(i, j, k)
    result = max(result, cnt)

print(result)
