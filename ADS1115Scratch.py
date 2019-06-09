# ADS1115 read analog

#import the Scratch data sender
import SensorUpdateScratch
# Import the ADS1x15 module.
import Adafruit_ADS1x15
import time


# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115() 
#Set Default Analog Channel Gain
GAIN = 1
ch0_value = adc.read_adc(0, GAIN)
ch1_value = adc.read_adc(1, GAIN)
ch2_value = adc.read_adc(2, GAIN)
ch3_value = adc.read_adc(3, GAIN)


A0 = SensorUpdateScratch.ScratchSensorUpdate('127.0.0.1', 42001, 'ADS1115_A0', ch0_value)
A1 = SensorUpdateScratch.ScratchSensorUpdate('127.0.0.1', 42001, 'ADS1115_A1', ch1_value)
A2 = SensorUpdateScratch.ScratchSensorUpdate('127.0.0.1', 42001, 'ADS1115_A2', ch2_value)
A3 = SensorUpdateScratch.ScratchSensorUpdate('127.0.0.1', 42001, 'ADS1115_A3', ch3_value)

while True:
	A0.sensorValue = adc.read_adc(0, GAIN)
	A1.sensorValue = adc.read_adc(1, GAIN)
	A2.sensorValue = adc.read_adc(2, GAIN)
	A3.sensorValue = adc.read_adc(3, GAIN)
	

	A0.sendUpdate()
	A1.sendUpdate()
	A2.sendUpdate()
	A3.sendUpdate()
	
	
	time.sleep(0.2)
if __name__ == '__main__' :
				
				print('Reading ADS1x15 values, press Ctrl-C to quit...')
				# Print nice channel column headers.
				print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
				print('-' * 37)
				
