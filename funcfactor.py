def factor(n):
	for i in range(1,n+1):
		if(n%i==0):
			print(i)
num=int(input("enter the number:"))
factor(num)