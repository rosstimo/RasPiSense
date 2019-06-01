import random

class dummy():

	def __init__(self, command, pins, interval):
		'''Initialise Sensor'''
		self.name = 'dummy'
		self.command = command
		self.pins = pins
		self.interval = interval

	def get(self):
		return random.randint(0,100)
		
	def value(self):
		'''get sensor value from IO interface'''
		pass
	
	def continuous(self,interval):
		'''Send data continuously until stop command recieved'''
		pass
		
	def setupInterface(self):
		'''setup interface'''
		pass
	
	def resetInterface(self):
		'''Reset interface to default or safe state'''
		pass
	
def fakeValue():
	'''Return fake random value'''
	pins = (4, 7)
	d = dummy(pins)
	print(d.get(), d.pins[0])


print(__name__)

if __name__ == '__main__' :
	fakeValue()
print(help(dummy))
