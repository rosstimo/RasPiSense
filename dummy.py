import random
import socket

class dummy():

	def __init__(self, command, pins, interval):
		'''Initialise Sensor'''
		self.name = 'dummy'
		self.command = command
		self.pins = pins
		self.interval = interval
		#self.value = value()

	def get(self):
		return random.randint(0,100)
		#self.value() = random.randint(0,100)

	def value(self):
		'''get sensor value from IO interface'''
		return random.randint(0,100)

	def continuous(self,interval):
		'''Send data continuously until stop command recieved'''
		pass

	def setupInterface(self):
		'''setup interface'''
		pass

	def resetInterface(self):
		'''Reset interface to default or safe state'''
		pass






#def fakeValue():
	'''Return fake random value'''
command = 'get'
pins = (4, 7)
interval = 0
d = dummy(command, pins, interval)

	#print(d.get(), d.pins[0])

print(dummy.value(d))


print(__name__)

if __name__ == '__main__' :
	print(d)
	print('command is ' + str(d.command))
	print('pin 0 is ' + str(d.pins[0]))
	print('interval is ' + str(d.interval))
	print('value is ' + str(d.value()))
#print(help(dummy))
