t = int(input())

for i in range(t):
	x = int(input())
	arr = []
	for k in range(x+1):
		y = str(bin(k))
		c = y.count('1')
		arr.append(c)
	print(arr)
			