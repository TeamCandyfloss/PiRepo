import smbus
import time
import socket
bus = smbus.SMBus(1)
UDP_IP = "192.168.6.169"
UDP_PORT = 9877
MESSAGE = "Hello"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Broadcaster")
print("crtl+c tp stop")

bus.write_byte(0x48, 0x00)
#0x00 lysmåler
#0x01 anden ting
#0x02 temp måler
#0x03 potientititi

last_reading = -1

while(True):
	
	reading = bus.read_byte(0x48)
	if(abs(last_reading - reading) > 2):
		print(reading)
		last_reading = reading
		message = (str(last_reading))
		#message = "56"
		sock.sendto(bytes(message, 'UTF-8'),(UDP_IP, UDP_PORT))
		time.sleep(0.5)
	
