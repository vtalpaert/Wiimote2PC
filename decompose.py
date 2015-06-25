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
