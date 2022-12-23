class publisher:
	pub_name=""
	pub_address=""
	def __init__(self):
		self.pub_name="DC"
		self.pub_address="BBI Books"
	def adddetails(self):
		self.pub_name=input("enter the publisher name::")
		self.pub_address=input("enter the address of the publisher::")
class book(publisher):
	book_name=""
	author_name=""
	def __init__(self):
		self.book_name=input("enter the book name::")
		self.author_name=input("enter the author name::")
class pythonbook(book):
	price=0.0
	no_of_pages=0
	def __init__(self):
		self.price=float(input("enter the price of the book::"))
		self.no_of_pages=int(input("enter the number of pages::"))
		super().__init__()
	def adddetails(self):
		self.pub_name=input("enter the publisher name::")
		self.pub_address=input("enter the address of the publisher::")
	def display(self):
		print("BOOK DETAILS!!!")
		print("BOOK NAME=",self.book_name)
		print("AUTHOR NAME=",self.author_name)
		print("PRICE OF THE BOOK=",self.price)
		print("NO OF PAGES=",self.no_of_pages)
		print("PUBLISHER NAME=",self.pub_name)
		print("OUBLISHER ADDRESS=",self.pub_address)
ob=pythonbook()
ob.adddetails()
ob.display()	
