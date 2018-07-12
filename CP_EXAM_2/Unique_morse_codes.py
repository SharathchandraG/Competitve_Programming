dict1 = {
'A': '.-',
'B': "-...",
'C': "-.-.",
'D': "-..",
'E': ".",
'F': "..-.",
'G': "--.",
'H': "....",
'I': "..",
'J': ".---",
'K': "-.-",
'L': ".-..",
'M': "--",	
'N': "-.",
'O': "---",
'P': ".--.",
'Q': "--.-",
'R': ".-.",
'S': "...",
'T': "-",
'U': "..-",
'V': "...-",
'W': ".--",
'X': "-..-",
'Y': "-.--",
'Z': "--.."	}


t = int(input())

for k in range(t):
	words = eval(input())
	x = 0
	result = {}
	for word in words:
		res_str = ''
		for i in word:
			res_str = res_str + dict1[(i.upper())]
		if result.get(res_str) is not None:
			pass
		else:
			x += 1
		result[res_str] = 0
	print(x)
