def pyramid(n):
	for i in range(0,n):
		space=' '
		for j in range(0,i+1):
			space=space+str(" * ")+" "
		print(space)
		print(" ")
	for p in range(n-1,0,-1):
		c=' '
		for q in range(1,p+1):
			c=c+str(" * ")+" "
		print(c)
		print(" ")
n=int(input("enter the number:"))
pyramid(n)
