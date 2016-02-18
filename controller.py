# code for receiving to pwm levels and sending to the controller




def setPWM(pwm):
	print(pwm)
# does nothing for now, obviously


# calculate PWM factors (0 to 100) from cleanacc = (rotation, speed)
# again, with some maths:
def pwm(cleanacc):
	rot = cleanacc[0]
	speed = cleanacc[1]
	candidate1 = (speed*1./25 - 2)*rot + 100 - speed
	candidate2 = (2 - speed*1./25)*rot + 3 * speed - 100
	if (speed > 50):
		pwm1 = min(speed, candidate1)
		pwm2 = min(speed, candidate2)
	else:
		pwm1 = max(speed, candidate1)
		pwm2 = max(speed, candidate2)
	return (pwm1, pwm2)


#init
oldcleanacc = (50,50)
#import turtlewii_func
#turtlewii_func.init()
def send_cleanacc(cleanacc):
	# use this to send a PWM to a controller
	#oldcleanacc = old
	if (oldcleanacc != cleanacc):
		old = cleanacc
		setPWM(pwm(cleanacc))

	# use this to visualise on screen with the turtle
	#turtlewii_func.move(cleanacc)


