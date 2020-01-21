#!/usr/bin/python
#Install pynmea2 library
#Refer https://github.com/Knio/pynmea2 for installation

import serial,pynmea2,time,datetime
import nanostation as ns
import subprocess,os
from time import mktime

port = serial.Serial("/dev/ttyUSB0", baudrate=9600)


t = datetime.datetime.now()
unix_secs = mktime(t.timetuple())


ssid=ns.extssid()
B_ID,CPE_IP=ns.mapip(ssid)
boat=B_ID
print CPE_IP
a=1
while a:
	rcv = port.readline()
#	print rcv[0:6]
	if rcv[0:6] == '$GPGGA':
		msg=pynmea2.parse(rcv)
		#print msg
		lat=msg.lat
		lat=pynmea2.dm_to_sd(lat)
		#print type (lat)
		lon=msg.lon
		lon=pynmea2.dm_to_sd(lon)
		#print lon
	if rcv[0:6] == '$GPRMC':
		msg=pynmea2.parse(rcv)
		#print msg
		speed=msg.spd_over_grnd
		#print speed
		a=0
temp=subprocess.check_output(["vcgencmd","measure_temp"])
temp=temp.replace("temp=","").replace("'C\n","")
#print temp
data={'time':unix_secs,'BOAT':boat,'lat':lat,'lon':lon,'speed':speed,'temp':temp}
print data
conn.close()
print "GPS Updated"
#except IndexError:
        # print("To catch an error...")
 #       continue
#except KeyboardInterrupt:
 #       print("\nProgram stopped.")
  #      exit()
