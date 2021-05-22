import sys

dx = [1, -1, 0, 0] 
dy = [0, 0, 1, -1]

def dfs(x, y, h): 
    for i in range(4): 
        nx = x + dx[i] 
        ny = y + dy[i] 
        if(0 <= nx < N) and (0 <= ny < N): 
            if arr[nx][ny] > h and done[nx][ny] == 0: 
                done[nx][ny] = 1 
                dfs(nx, ny, h)

N = int(input()) 
arr = [list(map(int, input().split())) 
for _ in range(N)] ans = 0 for k in range(max(map(max, arr))): 
    cnt = 0 
    done = [[0]*N for _ in range(N)] # 입력 받은 arr배열 탐색 
    for i in range(N): 
        for j in range(N): 
            if arr[i][j] > k and done[i][j] == 0: 
                done[i][j] = 1 
                cnt += 1 
                dfs(i, j, k) 
    ans = max(ans, cnt)

print(ans)
