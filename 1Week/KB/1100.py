import sys
board = [sys.stdin.readline() for _ in range(8)]

odd = [1, 3, 5, 7]
even = [0, 2, 4, 6]
count = 0

for i in range(len(board)):
    search = even
    if i%2 == 1:
        search = odd

    for j in search:
        if board[i][j] == 'F':
            count += 1

print(count)
