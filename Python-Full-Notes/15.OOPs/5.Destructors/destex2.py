#here PVM calls Garbage Collector  and  Garbage Collector inturns calls its own destructor for de-allocating the memory space.
#destex2.py
import time
class Employee:
	def __init__(self,eno,ename,sal):
		print("I am from Constructor:")
		self.eno=eno
		self.ename=ename
		self.sal=sal
		print("{}\t{}\t{}".format(self.eno,self.ename,self.sal))

	def	__del__(self): # Programmer-defined Destructor
		print("\nDestructor called by Garbage Collector:")

#main program
print("Line-15-->Program execution Started:")
eo1=Employee(10,"RS",34.56)
print("No longer interested to maintain eo1 object data")
time.sleep(5)
eo1=None # GC Calls __del__(self)--Forcefully we are calling GC--eo1
eo2=Employee(20,"DR",44.56)
eo3=Employee(30,"MC",24.56)
print("Line-21-->Program execution ended:")
 # GC Calls __del__(self)--automatically  calling GC--eo2 and eo3