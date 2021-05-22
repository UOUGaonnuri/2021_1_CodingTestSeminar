import sys
from collections import deque


def BFS(r, c):
    global N, M, field
    q = deque([(r, c)])
    field[r][c] = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    size = 1

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < M and field[ny][nx]:
                q.append((ny, nx))
                field[ny][nx] = 0
                size += 1
    
    return size

N, M, K = map(int, sys.stdin.readline().rstrip().split())
field = [[0 for i in range(M)] for j in range(N)]

for _ in range(K):
    r, c = map(int, sys.stdin.readline().rstrip().split())
    field[r-1][c-1] = 1

size = -1
for i in range(N):
    for j in range(M):
        if field[i][j]:
            size = max(size, BFS(i, j))

print(size)
