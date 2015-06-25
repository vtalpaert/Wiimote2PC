# This program utilises the cwiid Python library in order to get input over bluetooth from a wiimote.
# Coded by The Raspberry Pi Guy. Work based on some of Matt Hawkins's!

# Modified by Victor Talpaert, June 2015.
# The aim is to react to some buttons combinations

import cwiid, time, extra, turtlewii


button_delay = 0.1

# dictionnary - button mapping in power of 2

HOME = 7




time.sleep(1)

# This code attempts to connect to your Wiimote and if it fails the program quits
try:
  wii=cwiid.Wiimote()
except RuntimeError:
  quit()

time.sleep(1)

wii.rpt_mode = cwiid.RPT_BTN

wii.led = 1

print('data = [...')

while True:

  	buttons = wii.state['buttons']

  	# Detects whether + and - are held down and if they are it quits the program
  	if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
    		# NOTE: This is how you RUMBLE the Wiimote
    		wii.rumble = 1
    		time.sleep(0.1)
    		wii.rumble = 0
    		exit(wii)


  	
  	if (buttons & cwiid.BTN_HOME):
    		wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
    		check = 0
    		while check == 0:
			cleanacc = extra.coeffcalc(wii.state['acc'])
      			# print(cleanacc)
			if (cleanacc != (0, 0)):
				turtlewii.move(cleanacc)
      			time.sleep(0.01)
      			check = (buttons & cwiid.BTN_HOME)
    		time.sleep(button_delay)


