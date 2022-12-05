def wordcount(w):
	b={}
	for i in w:
		if i in b:
			b[i]+=1
		else:
			b[i]=1
	print("the count of all character:",b)
l1=list(input("\n enter the string:"))
wordcount(l1)