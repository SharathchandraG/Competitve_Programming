n = int(input())

for k in range(n):
	s = input().lower()
	t = input().lower()

	l1 = [0]*26

	for i in s:
		if not i == ' ':
			l1[ord(i) - 97] += 1
	for i in t:
		if not i == ' ':
			l1[ord(i) - 97] -= 1
	if (l1 == [0]*26):
		print("True")
	else:
		print("False")	