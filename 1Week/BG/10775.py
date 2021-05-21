import sys

input = sys.stdin.readline
G = int(input())
P = int(input())
gate = [0 for _ in range(G+1)]
num = [int(input()) for _ in range(P)]

docking = 0

for i in num:
    while i > 0:
        if gate[i] == 0:
            gate[i] = 1
            docking += 1
            break
        i -= 1
    if i == 0:
        break

print(docking)
