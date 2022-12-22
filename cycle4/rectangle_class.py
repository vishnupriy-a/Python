class rectangle:
	length=0
	breadth=0
	def __init__(self,l,b):
		self.length=l
		self.breadth=b
	def area(self):
		self.area1=self.length*self.breadth
		return self.area1
	def peri(self):
		peri=2*(self.length + self.breadth)
		return peri

obj1 = rectangle(5, 4)
obj2 = rectangle(4, 5)

print("Area of first rectangle is:", obj1.area())
print("Area of second rectangle is: ", obj2.area())
print("Perimeter of first rectangle is:", obj1.peri())
print("Perimeter of second rectangle is:", obj2.peri())

if (obj1.area() == obj2.area()):
	print("Areas of both rectangles are equal")
else:
	if (obj1.area() > obj2.area()):
		print("Area of first rectangle is greater\n")
	else:
		print("Area of second rectangle is greater")
