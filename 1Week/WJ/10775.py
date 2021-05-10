G = int(input())
P = int(input())

input = []

for i in range(P):
    a = int(input())
    if a >= 1 and a <= G:
        input.append(a)

input.sort()

for i in range(input):

