import RPi.GPIO as GPIO
import time
def blinkShort(pin):
	GPIO.output(pin, GPIO.HIGH)
	time.sleep(0.25)
	GPIO.output(pin,GPIO.LOW)
	time.sleep(0.25)
	return
def blinkLong(pin):
	GPIO.output(pin, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(pin,GPIO.LOW)
	time.sleep(0.5)
	return
def wait(pin):
	GPIO.output(pin,GPIO.LOW)
	time.sleep(1)
	return

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)


print ('Enter Your Message: ')
x = (raw_input())

y = len(x)
tyler = 0
for tyler in xrange(0,y):
	if x[tyler] == "a":	
		blinkShort(18) 
		blinkLong(18)
		wait(18)
                
	elif x[tyler] == "b":
		blinkLong(18)
		blinkShort(18)
		blinkShort(18)
		blinkShort(18)
		wait(18)
	elif x[tyler] == "c":
		blinkLong(18)
		blinkShort(18)
		blinkShort(18)
		blinkShort(18)
		wait(18)
	elif x[tyler] == "d":
		blinkLong(18)
		blinkShort(18)
		blinkShort(18)
		wait(18)
	elif x[tyler] == "e":
		blinkShort(18)
		wait(18)
	elif x[tyler] == "f":
		blinkShort(18)
		blinkShort(18)
		blinkLong(18)
		blinkShort(18)
		wait(18)
	elif x[tyler] == "g":
		blinkLong(18)
		blinkLong(18)
		blinkShort(18)
		wait(18)
	elif x[tyler] == "h":
		blinkShort(18)
		blinkShort(18)
		blinkShort(18)
		blinkShort(18)
		wait(18)
	elif x[tyler] == "i":
		blinkShort(18)
		blinkShort(18)
		wait(18)
	elif x[tyler] == "j":
		blinkShort(18)
		blinkLong(18)
		blinkLong(18)
		blinkLong(18)
		wait(18)
	elif x[tyler] == "k":
		blinkLong(18)
		blinkShort(18)
		blinkLong(18)
		wait(18)
	elif x[tyler] == "l":
		blinkShort(18)
		blinkLong(18)
		blinkShort(18)
		blinkShort(18)
		wait(18)
	elif x[tyler] == "m":
		blinkLong(18)
		blinkLong(18)
		wait(18)
	elif x[tyler] == "n":
		blinkLong(18)
		blinkShort(18)
		wait(18)
	elif x[tyler] == "o":
		blinkLong(18)
		blinkLong(18)
		blinkLong(18)
		wait(18)
	elif x[tyler] == "p":
		blinkShort(18)
		blinkLong(18)
		blinkLong(18)
		blinkShort(18)
		wait(18)
	elif x[tyler] == "q":
		blinkLong(18)
		blinkLong(18)
		blinkShort(18)
		blinkLong(18)
		wait(18)
	elif x[tyler] == "r":
		blinkShort(18)
		blinkLong(18)
		blinkShort(18)
		wait(18)
	elif x[tyler] == "s":
		blinkShort(18)
		blinkShort(18)
		blinkShort(18)
		wait(18)
	elif x[tyler] == "t":
		blinkLong(18)
		wait(18)
	elif x[tyler] == "u":
		blinkShort(18)
		blinkShort(18)
		blinkLong(18)
		wait(18)
	elif x[tyler] == "v":
		blinkShort(18)
		blinkShort(18)
		blinkShort(18)
		blinkLong(18)
		wait(18)
	elif x[tyler] == "w":
		blinkShort(18)
		blinkLong(18)
		blinkLong(18)
		wait(18)
	elif x[tyler] == "x":
		blinkLong(18)
		blinkShort(18)
		blinkShort(18)
		blinkLong(18)
		wait(18)
	elif x[tyler] == "y":
		blinkLong(18)
		blinkShort(18)
		blinkLong(18)
		blinkLong(18)
		wait(18)
	elif x[tyler] == "z":
		blinkLong(18)
		blinkLong(18)
		blinkShort(18)
		blinkShort(18)
		wait(18)
	elif x[tyler] == " ": wait(18)
	elif x[tyler] == ".":
		blinkShort(18)
		blinkLong(18)
		blinkShort(18)
		blinkLong(18)
		blinkShort(18)
		blinkLong(18)
	elif x[tyler] == ",":
		blinkLong(18)
		blinkLong(18)
		blinkShort(18)
		blinkShort(18)
		blinkLong(18)
		blinkLong(18)
	elif x[tyler] == "?":
		blinkShort(18)
		blinkShort(18)
		blinkLong(18)
		blinkLong(18)
		blinkShort(18)
		blinkShort(18)
	tyler +=1


GPIO.cleanup()

 
