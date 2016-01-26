# -*- coding: utf-8 -*-

import serial
import commands
import RPi.GPIO as GPIO
import time
import warnings

def moduleCall(command, exString, row, timeout):
	try:
		port = serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=1)
	except:
		return "SERIAL_ERROR" 
	start= time.time()	

	at = command

	port.write(at+"\r")

	data = ""
	flag = 0
	cnt = 0
	result = ""

	while True:

		ctime= time.time()-start
		if ctime > timeout :
			result="TIMEOUT"
			break

		if port.inWaiting() > 0 :
			tmp = port.read(1)
			if tmp == "\r":
				if data == at:
					data = ""

				continue
			elif tmp == "\n":
				cnt = cnt + 1
				flag = 1
			else:
				data = data+tmp

		
		if flag == 1:
			if cnt == row:
				result = data

			if data == exString:
				#print "OK exit"
				data = ""
				flag = 0
				break
			elif data == "REJECT" or data == "ERROR":
				result = data
				data = ""
				flag = 0
				break
			else:
				data = ""
				flag = 0

	port.close()

	return result

def getVersion():
	ret= moduleCall("at+gmr", "OK", 1, 1.0)
	if ret.startswith("+GMR: "):
		return ret.split(" ")[1]
	else:
		return ret

def getDatetime():
	return moduleCall("at$31?", "OK", 1, 1.0)

def getPacketstat():
	return moduleCall("at$36?", "OK", 1, 1.0)
	
def getSimstat():
	return moduleCall("at$20?", "OK", 1, 1.0)
	
def getTelno():
	return moduleCall("at$21?", "OK", 1, 1.0)

def getIccid():
	return moduleCall("at$19?", "OK", 1, 1.0)
	
def getArea():
	return moduleCall("at+cad?", "OK", 1, 1.0)
	
def getAntenna():
	return moduleCall("at$30=0", "OK", 1, 1.0)

def getAntena():
  print('[deprecated] use getAntenna() instead')
  return getAntenna()
	
def getGpsid():
	return moduleCall("at@74?", "OK", 1, 1.0)

def getGpspass():
	return moduleCall("at@75?", "OK", 1, 1.0)
	
def setIpaddress(ip):
	if False == ip.startswith("192.168.225."):
		return "ERROR"
	i= int(ip.split(".")[3])
	if i < 8 or 224 < i:
		return "ERROR"
	commands.getoutput("ifconfig usb0 "+ip)
	commands.getoutput("route add -net 0.0.0.0 gw 192.168.225.1 netmask 0.0.0.0 usb0")
	commands.getoutput("route del -net 0.0.0.0 eth0")
	return "OK"
	
def setDmzip(ip):
	return moduleCall("at+dmzip="+ip, "OK", 2, 1.0)
	
def setSelectsim():
	return moduleCall("at$18=2", "OK", 2, 1.0)
	
def setGpsid(id):
	return moduleCall("at@74="+id, "OK", 2, 1.0)
	
def setGpspass(p,mode):
	return moduleCall("at@75="+p+","+mode, "OK", 2, 1.0)
	
def reqConnect(apn,id,p):
	ret= moduleCall("at$52=2", "OK", 2, 1.0)
	if ret != "OK":
		return ret
	ret= moduleCall("at+aapn="+apn, "OK", 2, 1.0)
	if ret != "OK":
		return ret
	ret= moduleCall("at+ccallid="+id+","+p+",1,0", "OK", 2, 1.0)
	if ret != "OK":
		return ret
	ret= moduleCall("at+ccall=1", "OK", 2, 5.0)
	if ret != "OK":
		return ret
	return "OK"
	
def reqDisconnect():
	return moduleCall("at+ccall=0", "OK", 2, 5.0)
	
def reqOta():
	return moduleCall("at@30", "OK", 2, 0.5)
	
def reqGpsStart(id,p,timeout):
	ret= moduleCall("at@74="+id, "OK", 2, 1.0)
	if ret != "OK":
		return ret
	ret= moduleCall("at@75="+p+",0", "OK", 2, 1.0)
	if ret != "OK":
		return ret
	ret= moduleCall("at@72", "OK", 2, 1.0)
	if ret != "OK":
		return ret
	return moduleCall("", "GPSOK", 1, timeout)
	
def reqGpsStop():
	return moduleCall("at@73", "OK", 2, 1.0)

def reqInit():
	return moduleCall("at&f0", "OK", 2, 2.0)
	
def reqWrite():
	return moduleCall("at&w0", "OK", 2, 1.0)
	
def reqVbusOn():
	#commands.getoutput("echo 5 > /sys/class/gpio/export")
	#commands.getoutput("echo out > /sys/class/gpio/gpio5/direction")
	commands.getoutput("echo 1 > /sys/class/gpio/gpio5/value")	
	return "OK"

def reqVbusOff():
	#commands.getoutput("echo 5 > /sys/class/gpio/export")
        #commands.getoutput("echo out > /sys/class/gpio/gpio5/direction")
        commands.getoutput("echo 0 > /sys/class/gpio/gpio5/value")
	return "OK"

def reqPowerOn():
	commands.getoutput("echo 0 > /sys/class/gpio/gpio12/value")
	commands.getoutput("echo 1 > /sys/class/gpio/gpio12/value")
	time.sleep(2.2)
	commands.getoutput("echo 0 > /sys/class/gpio/gpio12/value")
	return "OK"
	
def reqPowerOff():
	commands.getoutput("echo 0 > /sys/class/gpio/gpio12/value")
        commands.getoutput("echo 1 > /sys/class/gpio/gpio12/value")
        time.sleep(2.5)
        commands.getoutput("echo 0 > /sys/class/gpio/gpio12/value")
	return "OK"

def getPsHold():
	return commands.getoutput("cat /sys/class/gpio/gpio20/value")

def getRi():
	return commands.getoutput("cat /sys/class/gpio/gpio16/value")

def getAreaInd():
	return commands.getoutput("cat /sys/class/gpio/gpio6/value")
