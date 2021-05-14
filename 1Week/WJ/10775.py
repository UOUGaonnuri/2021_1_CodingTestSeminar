G = int(input())
P = int(input())
ans = 1
inputs = []

for i in range(P):
    a = int(input())
    if a >= 1 and a <= G:
        inputs.append(a)

inputs.sort()
tmp = inputs[0]
for i in inputs:
    if i != tmp:
        tmp = i
        ans += 1
print(ans)
