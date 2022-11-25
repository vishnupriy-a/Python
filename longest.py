def length(a):
	temp=0
	for i in a:
		if(len(i)>0):
			temp=len(i)
			c=i
	print("The longest word is:",i,"of length",temp)
l1=list(input("Enter the strings:").split())
length(l1)
			
