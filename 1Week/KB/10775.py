# filter 이용 (시간 초과)
import sys
G = int(sys.stdin.readline())
P = int(sys.stdin.readline())

gate = [0 for i in range(G)]
count = 0

gi = [int(sys.stdin.readline()) for i in range(P)]
    
for i in range(len(gi)):
    current = gi[i]
    
    index = list(filter(lambda x: gate[x] == 0, range(current)))
    if len(index) == 0:
        break
    
    gate[index[-1]] = 1
    count += 1
        
print(count)



# 예외 처리 이용 (시간 초과)
'''
import sys
G = int(sys.stdin.readline())
P = int(sys.stdin.readline())

gate = [0 for i in range(G)]
count = 0

gi = [int(sys.stdin.readline()) for i in range(P)]
    
for i in range(len(gi)):
    current = gi[i]
    
    try:
        gate.index(0, 0, current)
    except:
        break

    j = current - 1
    while j >= 0:
        if gate[j] == 0:
            gate[j] = 1
            count += 1
            break
        j -= 1
        
print(count)
'''
