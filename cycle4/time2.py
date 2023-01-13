class Time:
	def __init__(self, hr, mts, sec):
		self.__sec = sec % 60
		self.__mts = mts%60 + sec//60
		self.__hr = hr + mts//60

	def __add__(self, other):
		ss = self.__sec + other.__sec
		mm = self.__mts + other.__mts
		hh = self.__hr + other.__hr

		return Time(hh, mm, ss)

	def __str__(self):
		return str(self.__hr) + " : "  + str(self.__mts) + " : " + str(self.__sec)

h1 = int(input("Hours: "))
m1 = int(input("Minutes: "))
s1 = int(input("Seconds: "))

h2 = int(input("Hours: "))
m2 = int(input("Minutes: "))
s2 = int(input("Seconds: "))

t1 = Time(h1, m1, s1)
t2 = Time(h2, m2, s2)

t3 = t1 + t2
print(t3)
