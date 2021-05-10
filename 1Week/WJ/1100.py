sum = 0

inputs = []
for i in range(8):
	a = input()
	inputs.append(a)
for i in range(8):
	for j in range(8):
		if (i + j) % 2 == 0:
			if inputs[i][j] == 'F':
				sum += 1

print(sum)