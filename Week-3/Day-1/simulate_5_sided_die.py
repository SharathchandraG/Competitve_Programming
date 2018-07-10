def rand5():

    # Implement rand5() using rand7()
    rand = rand7()
    return rand if rand <= 5 else rand5()

print('Rolling 5-sided die...')
print(rand5())

lst = [0] * 5

for i in range(10000):
	lst[rand5()-1] += 1

print(lst)

# infinity