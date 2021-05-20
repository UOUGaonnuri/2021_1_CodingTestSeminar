# N x N 배열
# 일단 n을 뺀다고 가정하자.
import sys


n = int(input())

# 도화지
graph = []
test = []
MAX_result = 0
MAX = 0

def dfs(x,y):
    #요긴 범위
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if test[x][y] == 0:
        test[x][y] = 1

        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)

        return True
    return False

# 지형도 그림
for i in range(n):
    graph.append(list(map(lambda x: int(x), input().split())))
    MAX = max(graph) # 행마다 가장 높은 지역을 얻어왔음.

MAX = max(MAX) # 그 중에서 으뜸.
# 그럼 제일 높은거 물 차이면 어차피 0이니까 100까지 갈 필요 없이 그 전에도 끝낼 수 있지 않는가? -> 시간 관리 좋아질 것으로 예상

# 문제 -> 그럼 그래프를 또 그리게 됨 -> 0/1로 구성된 그래프를 또 그려야함.
if int(MAX+1) <= 100:
    for k in range(MAX+1):
        print("k = ", k)
        for i in range(n):
            test.append(list(map(lambda x: 0 if int(x) - k > 0 else 1, graph[i])))
        result = 0
# 그리고 나서 그거에 해당하는 dfs를 넣어서 해결하도록 만든 건데;;;
        for l in range(n):
            for j in range(n):
                if dfs(l, j):
                    result += 1
        print("result = ", result)
        if MAX_result < result:
            MAX_result = result
        test.clear()

if MAX_result < result:
    MAX_result = result

print("MAX_result: ", MAX_result)


# 내 생각
# 1. NxN 배열을 받아야함
# 2. 그 높이 만큼 배열을 뺀 채로 받아와야함
# 3. DFS로 해결해볼 것

# 백준에서 NameError가 발생한 걸로 봐선 문제가 있는 거 같습니다. ㅠ