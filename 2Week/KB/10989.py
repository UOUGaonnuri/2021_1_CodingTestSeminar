n = int(input())
arr = [int(input()) for _ in range(n)]
count = [0] * (max(arr)+1)


for i in range(len(arr)):
    count[arr[i]] += 1
for i in range(len(count)):
    for j in range(count[i]):
        print(i)
