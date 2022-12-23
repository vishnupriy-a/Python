class timee:
	_hr=00
	_min=00
	_sec=00
	def read(self):
		self.hr=int(input("enter the hours::"))
		self.min=int(input("enter minutes::"))
		self.sec=int(input("enter seconds::"))
	def display(self,t2):
		hr=00
		min=00
		sec=00
		if(self.min+t2.min>60):
			hr=hr+(self.min+t2.min)//60
			print((self.min+t2.min)//60)
			print(hr)
			min=min+((self.min+t2.min)%60)
		else:
			min=self.min+t2.min
		if(self.sec+t2.sec>60):
			min=min+(self.sec+t2.sec)//60
			sec=sec+((self.sec+t2.sec)%60)
		else:
			sec=self.sec+t2.self
			hr=hr+self.hr+t2.hr
			return hr,min,sec
t1=timee()
t2=timee()
t1.read()
t2.read()
t3=t1+t2
print(t3)

