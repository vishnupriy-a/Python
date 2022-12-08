def sum(a):
	sum=0
	for i in a:
		sum=sum+i
	print("the sum of the digit is..",sum)
l1=list(map(int,input("enter the number:").split()))
sum(l1)




