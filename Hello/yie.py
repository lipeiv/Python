# yield

def foo(num):
	while num < 10:
	 	num += 1
	 	yield num

for n in foo(0):
	print(n)
