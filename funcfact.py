def factorial():
	num=int(input("enter a number"))
	fact=1
	for i in range(1,num+1):
		fact=fact*i;
	return fact
n=factorial()
print("Factorial is:",n)

