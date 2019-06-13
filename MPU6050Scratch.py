#https://pypi.org/project/mpu6050-raspberrypi/
#https://github.com/Tijndagamer/mpu6050

#sudo i2cdetect -y 1


import SensorUpdateScratch
import sys
import time
#import mpu6050
from mpu6050 import mpu6050
#create instance set I2C address
mpu = mpu6050(0x68)
accel_data = mpu.get_accel_data()
gyro_data = mpu.get_gyro_data()



mpu_temp = SensorUpdateScratch.ScratchSensorUpdate('127.0.0.1', 42001, 'MPU6050_temp', mpu.get_temp())

accel_x = SensorUpdateScratch.ScratchSensorUpdate('127.0.0.1', 42001, 'MPU6050_acclX', accel_data['x'])
accel_y = SensorUpdateScratch.ScratchSensorUpdate('127.0.0.1', 42001, 'MPU6050_acclY', accel_data['y'])
accel_z = SensorUpdateScratch.ScratchSensorUpdate('127.0.0.1', 42001, 'MPU6050_acclZ', accel_data['z'])

gyro_x = SensorUpdateScratch.ScratchSensorUpdate('127.0.0.1', 42001, 'MPU6050_gyroX', gyro_data['x'])
gyro_y = SensorUpdateScratch.ScratchSensorUpdate('127.0.0.1', 42001, 'MPU6050_gyroY', gyro_data['y'])
gyro_z = SensorUpdateScratch.ScratchSensorUpdate('127.0.0.1', 42001, 'MPU6050_gyroZ', gyro_data['z'])



while True:
	
	mpu_temp.sendUpdate()
	accel_data = mpu.get_accel_data()
	gyro_data = mpu.get_gyro_data()
	
	accel_x.sensorValue = accel_data['x']
	accel_y.sensorValue = accel_data['y']
	accel_z.sensorValue = accel_data['z']
	gyro_x.sensorValue = gyro_data['x']
	gyro_y.sensorValue = gyro_data['y']
	gyro_z.sensorValue = gyro_data['z']
	
	accel_x.sendUpdate()
	accel_y.sendUpdate()
	accel_z.sendUpdate()
	gyro_x.sendUpdate()
	gyro_y.sendUpdate()
	gyro_z.sendUpdate()
	
	time.sleep(.1)

if __name__ == '__main__' :
	
	print(mpu.get_temp())
	accel_data = mpu.get_accel_data()
	print(accel_data['x'])
	print(accel_data['y'])
	print(accel_data['z'])
	gyro_data = mpu.get_gyro_data()
	print(gyro_data['x'])
	print(gyro_data['y'])
	print(gyro_data['z'])
	
				
