def ing(s):
	l=len(s)
	str=s[l-3]+s[l-2]+s[l-1]
	if(str=='ing'):
		print(s+'ly')
	else:
		print(s+'ing')
		
i=input("\nEnter a string:")
ing(i)