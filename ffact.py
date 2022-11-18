def factorial(x):
	if x==1:
		return x
	else:
		return(x * factorial(x-1))
num=int(input("enter a number"))
value=factorial(num)
print("factorial is",value)

