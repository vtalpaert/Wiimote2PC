# supplementary file grouping usefull functions

# function transfroming the raw acceleration values into speed percentage and 'direction distribution' percentage (understand more to the left, middle or more to the right)
# speed: full reverse 0%, null 50%, full forward 100%
# rotation: to the left 0%, middle 50%, right 100% (might change)

# params
# x:
lowx = 100
highx = 150
# z:
lowz = 130
highz = 155

def ramp(t, low, high):
	print('yup')
	return min(100, 100*max(0, (t-low)/(high-low)))

def coeffcalc(rawacc):

	# params
	# x:
	lowx = 100
	highx = 150
	# z:
	lowz = 130
	highz = 155


	print('nah')
	return (self.ramp(rawacc[0], lowx, highx), self.ramp(rawacc[2], lowz, highz))	

