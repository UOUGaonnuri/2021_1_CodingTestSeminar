import sys
import copy
sys.setrecursionlimit(10000)

n = int(input())
loc = [list(map(int, input().split())) for _ in range(n)] 


def dfs(x, y, high):
    if x<0 or x>=n or y<0 or y>=n:
        return False
    
    if list_tmp[x][y] == 0:
        return False
    
    list_tmp[x][y] = 0
    if loc[x][y] > high:
        dfs(x-1, y, high)
        dfs(x+1, y, high)
        dfs(x, y+1, high)
        dfs(x, y-1, high)
        return True
    else:
        return False


result = 0
result_high = 0
for high in range(max(map(max, loc))):
    list_tmp = copy.deepcopy(loc)
    count = 0
    for i in range(n):
        for j in range(n):
            if dfs(i, j, high) == True:
                count += 1
    
        
    if result < count:
        result = count
        result_high = high
        
print('최대 영역 개수 : ' + str(result))
print('이때의 높이 : ' + str(result_high))
