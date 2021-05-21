import sys

n, m = map(int, sys.stdin.readline().split())

# print(n, m)

frame = []
for i in range(n):
    # 한 줄을 입력받고 각 원소를 정수형으로 리스트에 추가
    frame.append(list(map(int, input())))

# 값이 0인 노드를 방문 처리


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if frame[x][y] == 0:
        frame[x][y] = 1

        dfs(x, y-1)  # 상
        dfs(x, y+1)  # 하
        dfs(x-1, y)  # 좌
        dfs(x+1, y)  # 우

        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            # 해당 노드가 처음 방문일 때만 result 값 증가
            result += 1

print(result)
