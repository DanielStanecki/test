class Device:
	def __init__(self, height, width, name):
		self.name = name
		self.width = width
		self.height = height
	
	def powerOn(self):
		print("The power is on")

class Computer(Device):
	def powerOn(self):
		print("The computer is on")
	
	def loggingOn(self): 
		print("You are logging in")
	
	def powerOff(self): 
		print("The computer is off")


device1 = Device(300, 200, "phone")
device2 = Computer(100, 200, "dell")
device1.powerOn()