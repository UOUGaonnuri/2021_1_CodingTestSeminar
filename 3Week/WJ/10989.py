import sys

N = int(sys.stdin.readline().rstrip())
case = []
for _ in range(N):
    case.append(int(sys.stdin.readline().rstrip()))

case.sort()
for i in case:
    print(i)
