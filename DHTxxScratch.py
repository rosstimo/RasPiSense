# DHT11 read analog see https://tutorials-raspberrypi.com/raspberry-pi-measure-humidity-temperature-dht11-dht22/

import SensorUpdateScratch
import sys
import time
import Adafruit_DHT

# Create DHT22 or DHT11 instance.
DHTxx = Adafruit_DHT.DHT11
#DHTxx = Adafruit_DHT.DHT22

#Set Default GPIO pin
pin = 20
#try 15 times to get a reading
humidity, temperature = Adafruit_DHT.read_retry(DHTxx, pin)


DHT_humi = SensorUpdateScratch.ScratchSensorUpdate('127.0.0.1', 42001, 'DHTxx_Humidity', humidity)
DHT_temp = SensorUpdateScratch.ScratchSensorUpdate('127.0.0.1', 42001, 'DHTxx_Temperature', temperature)


while True:
	humidity, temperature = Adafruit_DHT.read_retry(DHTxx, pin)
	if humidity is not None:
		DHT_humi.sensorValue = humidity
	if temperature is not None:
		DHT_temp.sensorValue = temperature

	DHT_humi.sendUpdate()
	DHT_temp.sendUpdate()

	
	
	time.sleep(0.2)
if __name__ == '__main__' :
				
				print('Reading DHTxx values, press Ctrl-C to quit...')
				# Print nice channel column headers.
				print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
				print('-' * 37)
				
