t = int(input())

for i in range(t):
	x = str(bin(int(input())))
	x = x[2:]
	print(x)
	c = 0
	max_c = 0
	for k in range(len(x)):
		if x[k] == '1':
			c += 1
		elif x[k] == '0' :
			if (max_c < c):
				max_c = c
			c = 0
	print(max_c)