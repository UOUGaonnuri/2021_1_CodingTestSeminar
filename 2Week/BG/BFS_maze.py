import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

frame = []
for i in range(n):
    frame.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs - 간선의 비용이 모두 같을 때 최단거리를 구할 수 있는 알고리즘


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 괴물인 경우 무시
            if frame[nx][ny] == 0:
                continue

            if frame[nx][ny] == 1:
                frame[nx][ny] = frame[x][y] + 1
                queue.append((nx, ny))

    return frame[n-1][m-1]


print(bfs(0, 0))
