def fib(x):
	a=0
	b=1
	print(a)
	print(b)
	for i in range(1,x-1):
		c=a+b
		print(c)
		a=b
		b=c
num=int(input("\n Enter the number:"))
print("\n Fibonocci series...................\n")
fib(num)
    
