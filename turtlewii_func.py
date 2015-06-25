# small script just to play with some visuals
# too lazy to integrate the acceleration, we just iteratively move the turtle

import turtle, time

# param
distance = 30
sensibility = 0.1


# init
turtle.reset()
turtle.left(90)
turtle.pensize(5)
turtle.shape("turtle")
turtle.resizemode("auto")

def move(cleanacc):
	# cleanacc is (x, z)
	speed = 1./100*(cleanacc[1]-50) # variable multiplication factor of distance
	angle = sensibility*4.5*(cleanacc[0] - 50) # degrees
	print(cleanacc)
	print(speed, angle)
	if (speed > 0):
		turtle.right(angle)
	else:
		turtle.left(angle)
	turtle.forward(speed * distance)
