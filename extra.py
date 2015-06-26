# supplementary file grouping usefull functions


# function transfroming the raw acceleration values into speed percentage and 'direction distribution' percentage (understand more to the left, middle or more to the right)
# speed: full reverse 0%, null 50%, full forward 100%
# rotation: to the left 0%, middle 50%, right 100% (might change)

# params
# x:
lowx = 100
highx = 150
# z:
lowz = 105
highz = 155

def ramp(t, low, high):
	return min(100, 100*max(0, (t-low)*1./(high-low)))

def coeffcalc(rawacc):
	if (rawacc == (0, 0, 0)):
		return (50, 50)
	return (ramp(rawacc[0], lowx, highx), ramp(rawacc[2], lowz, highz))	




# I'm afraid we have to use... MATHS!!!! 

# function to decompose a number in a sum of power of 2
# input is number in base 10
# output list of the powers

def powers_of_2(x):
	s = str(bin(x)[2:]) # binary value of x
	l = len(s)
	result = []
	for i in range(l):
		if (s[l-1-i] == '1'):
			result.append(i)

    	return result

def increase(speed, factor):
	return min(100, speed + factor)

def decrease(speed, factor):
	return max(50, speed - factor) # watch out for the 50 instead of 0, on purpose
