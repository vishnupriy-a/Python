def pyramid(n):
	print("enter the pyramid:")
	for i in range(1,n+1):
		space=' '
		for j in range(1,i+1):
			space=space+str(i*j)+" "
		print(space)
n=int(input("enter the number:"))
pyramid(n)
 





















