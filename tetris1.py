import RPi.GPIO as GPIO
import time
import math

GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)

PIN1=7
PIN2=11
PIN3=12
PIN4=13
PIN5=15
PIN6=16
PIN7=18
PIN8=22
PINA=29
PINB=31
PINC=32
PIND=33
PINE=35
PINF=36
PING=37
PINH=38

matrix = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

def makeMatrix():
	for i in range(0,8):
		for j in range(0,8):
			#matrix[i][j]=randint(0,1)
			if i==j:
				matrix[i][j]=1
			else:
				matrix[i][j]=0

#randomize the matrix
#Positive:4cd7f621
#Negative:ebga5h38

def pinCol(name):
	if name==0:
		return PIN4
	elif name==1:
		return PINC
	elif name==2:
		return PIND
	elif name==3:
		return PIN7
	elif name==4:
		return PINF
	elif name==5:
		return PIN6
	elif name==6:
		return PIN2
	elif name==7:
		return PIN1
	else:
		print "hag diya"

def pinRow(name):
	if name==0:
		return PINE
	elif name==1:
		return PINB
	elif name==2:
		return PING
	elif name==3:
		return PINA
	elif name==4:
		return PIN5
	elif name==5:
		return PINH
	elif name==6:
		return PIN3
	elif name==7:
		return PIN8
	else:
		print "hag diya"


#try:
#while True:
#pass
for t in range(0,500):
	makeMatrix()
	for i in range(0,8):
		#i  wali pin high
		#GPIO.output(pinCol(i), HIGH)
		for j in range(0,8):
			if matrix[i][j]==1:
				pass
				#j wali transistor high/on
		#		GPIO.output(pinRow(j), HIGH)
			else:
				pass
				#transistor off
		#		GPIO.output(pinRow(j), LOW)
	time.sleep(0.01)
#except:
#	print "Error"
#makeMatrix()
for i in range(0,8):
		for j in range(0,8):
			print matrix[i][j]
