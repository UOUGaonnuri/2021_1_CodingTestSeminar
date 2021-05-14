import sys

G = int(sys.stdin.readline().rstrip("\n"))
P = int(sys.stdin.readline().rstrip("\n"))
plist = [int(sys.stdin.readline().rstrip("\n")) for i in range (0,P)]

def findParent(x):
   if parent[x] == x:
       return x
   p = findParent(parent[x])
   parent[x]=p
   return parent[x]

def unionParent(x,y):
    x = findParent(x)
    y = findParent(y)
    if x<y:
        parent[y] = x
    else:
        parent[x] = y
# 이중 반복문으로는 시간 초과 => union-find이용
parent = {i:i for i in range(0,G+1)}
count=0
for plist in plists:
    x = findParent(plist)
    if x==0:
        break
    unionParent(x,x-1)
    count+=1
print(count)
