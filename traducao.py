print("Hello, world!")
a = 1

b = 3

c = 5

print(a + b + c)
def printSum(a, b):
	print(a + b)
printSum(10, 15)

def getSum(a, b):
	return a + b
sum = getSum(4, 5)

if sum > 10:
	print("yes")
elif sum > 20:
	print("maybe")
else:
	print("no")

def a1(a):
	return a * 2
def a2(b):
	return a / 2
print(a1(4) * a2(10))
print(a2(5) / a1(50))
c = None

if a1(4) > 5:
	print("ok")

c = 40

print(c)
