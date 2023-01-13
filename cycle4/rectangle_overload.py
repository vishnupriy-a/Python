class rectangle:
	length=0
	breadth=0
	def __init__(self,l,b):
		self.length=l
		self.breadth=b
	def area(self):
		self.area1=self.length*self.breadth
		return self.area1
	def __lt__(self, other):
		return self.area() < other.area()

obj1 = rectangle(5, 4)
obj2 = rectangle(4, 5)

print("Area of first rectangle is:", obj1.area())
print("Area of second rectangle is: ", obj2.area())

if (obj1 < obj2):
	print("Area of first rectangle is lesser\n")
else:
	print("Area of second rectangle is less than or equal")
