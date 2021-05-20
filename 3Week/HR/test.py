# N x N 배열
# 일단 n을 뺀다고 가정하자.
import time


n = int(input())

# 도화지
graph = []
result = 0
for i in range(n):
    graph.append(list(map(lambda i: 0 if int(i)-6 > 0 else 1, input().split())))

print(graph)

def dfs(x,y):
    #요긴 범위
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1

        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)

        return True
    return False




for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result += 1

print(graph)
print(result)
#print(time.time() - start)

# 내 생각
# 1. NxN 배열을 받아야함
# 2. 그 높이 만큼 배열을 뺀 채로 받아와야함
# 3. DFS로 해결해볼 것

# 이중 for문 문제가 발생할 수 있으므로 map(lambda)로 해결

# 문제점: 입력값은 NxN의 N과 높이만 입력을 받아서 실제로 물 높이가 어떤지를 알 길이 없어 해결을 못함