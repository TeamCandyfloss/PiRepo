import RPi.GPIO as GPIO
import time
import dht11
import socket
UDP_IP = "192.168.3.239"
UDP_PORT = 9877
MESSAGE = "Hello"
lasttemp = 255
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
iteration = 1

#initialize
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(3, GPIO.IN)


# read data using pin 3


while True:

	#lasthumid = humid
	
	instance = dht11.DHT11(pin = 3)
	result = instance.read()
	
	
	
	if result.is_valid():
		temp = result.temperature
		humid = result.humidity
		
	
		print("Temperature: %d C" % result.temperature)
		print("Humidity: %d %%" % result.humidity)

		message = (str(temp)) #+ (str(humid))
		#message = "56"
		sock.sendto(bytes(message, 'UTF-8'),(UDP_IP, UDP_PORT))
		print(iteration)
		iteration += 1
		
	else:
		print("Error: %d" % result.error_code)
		
		

		
		
	time.sleep(30.0)
	
	
	
# try:
	# while True:
		# i = GPIO.input(3)

		# print(i)
		# time.sleep(0.5)

	

	
	
# finally:
	
	# GPIO.cleanup()