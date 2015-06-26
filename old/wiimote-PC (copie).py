# This program utilises the cwiid Python library in order to get input over bluetooth from a wiimote.
# Coded by The Raspberry Pi Guy. Work based on some of Matt Hawkins's!

# Modified by Victor Talpaert, June 2015.
# The aim is to react to some buttons combinations

import cwiid, time, decompose


button_delay = 0.1

# dictionnary - button mapping in power of 2
B2 = 0 # Button 2
B1 = 1 # Button 1
TRIGGERB = 2
A = 3
MINUS = 4
HOME = 7
LEFT = 8
RIGHT = 9
DOWN = 10
UP = 11
PLUS = 12


print 'Please press buttons 1 + 2 on your Wiimote now ...'
time.sleep(1)

# This code attempts to connect to your Wiimote and if it fails the program quits
try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print "Cannot connect to your Wiimote. Run again and make sure you are holding buttons 1 + 2!"
  quit()

print 'Wiimote connection established!\n'
print 'Go ahead and press some buttons\n'
print 'Press PLUS and MINUS together to disconnect and quit.\n'

time.sleep(3)

wii.rpt_mode = cwiid.RPT_BTN

while True:

  	buttons = wii.state['buttons']

	powers = decompose.powers_of_2(buttons)


  	# Detects whether + and - are held down and if they are it quits the program
  	if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
    		print '\nClosing connection ...'
    		# NOTE: This is how you RUMBLE the Wiimote
    		wii.rumble = 1
    		time.sleep(0.1)
    		wii.rumble = 0
    		exit(wii)


  	if (UP in powers):
		if (LEFT in powers):
    			print 'Up-Left'
    			time.sleep(button_delay)
		elif (RIGHT in powers):
			print 'Up-Right'
    			time.sleep(button_delay)
		else:
			print 'Up'
    			time.sleep(button_delay)
	elif (DOWN in powers):
		if (LEFT in powers):
    			print 'Down-Left'
    			time.sleep(button_delay)
		elif (RIGHT in powers):
			print 'Down-Right'
    			time.sleep(button_delay)
		else:
			print 'Down'
    			time.sleep(button_delay)

  	elif (LEFT in powers):
    		print 'Left'
    		time.sleep(button_delay)
  	elif (RIGHT in powers):
    		print 'Right'
    		time.sleep(button_delay)

  	if (A in powers):
    		print 'A'
    		time.sleep(button_delay)
  	if (TRIGGERB in powers):
    		print 'B'
    		time.sleep(button_delay)

  	if (B1 in powers):
    		print 'B1'
    		time.sleep(button_delay)
  	if (B2 in powers):
    		print 'B2'
    		time.sleep(button_delay)

  	if (PLUS in powers):
    		print 'Plus'
    		time.sleep(button_delay)
  	if (MINUS in powers):
    		print 'Minus'
    		time.sleep(button_delay)


  	if (buttons & cwiid.BTN_HOME):
    		wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
    		check = 0
    		while check == 0:
      			print(wii.state['acc'])
      			time.sleep(0.01)
      			check = (buttons & cwiid.BTN_HOME)
    		time.sleep(button_delay)


