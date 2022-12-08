def word(x):
	l=0
	for i in x:
		if(len(i)>l):
			l=len(i)
			m=i
	print("The longest word is",m)
	print(l)
num=input("enter the list of words:").split()
word(num)
		
