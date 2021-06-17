import sys
input = lambda : sys.stdin.readline().rstrip()

def bs(size, a, m):
    low = 0
    high = size - 1
    while low <= high:
        mid = low+(high-low)/2
        if a[mid] < m:
            low = mid + 1
        elif a[mid] > m:
            high = mid -1
        else:
            return true
    return false

T = int(input())
while T >= 0:
    N = int(input())
    a = []
    for i in range(N):
        a.append(int(input()))
    a.sort()
    M = int(input())
    while M >= 0:
        t = int(input())
        print(bs(N,a,t))