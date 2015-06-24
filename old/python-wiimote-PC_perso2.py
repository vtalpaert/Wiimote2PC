# Modified by Victor Talpaert, June 2015.
# It appears it the Wiimote cannot recognize a combination LEFT + RIGHT or UP + DOWN



# This program utilises the cwiid Python library in order to get input over bluetooth from a wiimote.
# Coded by The Raspberry Pi Guy. Work based on some of Matt Hawkins's!

import cwiid, time

button_delay = 0.1

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

  # Detects whether + and - are held down and if they are it quits the program
  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
    print '\nClosing connection ...'
    # NOTE: This is how you RUMBLE the Wiimote
    wii.rumble = 1
    time.sleep(0.3)
    wii.rumble = 0
    exit(wii)




  if (buttons & cwiid.BTN_UP):
	if (buttons & cwiid.BTN_LEFT):
		print 'Up-Left pressed'
    		time.sleep(button_delay)
	elif(buttons & cwiid.BTN_RIGHT):
		print 'Up-Right pressed'
    		time.sleep(button_delay)	
	else:
		print 'Up pressed'
    		time.sleep(button_delay)
  else:
	


  if (buttons & cwiid.BTN_LEFT):
    print 'Left pressed'
    time.sleep(button_delay)

  if(buttons & cwiid.BTN_RIGHT):
    print 'Right pressed'
    time.sleep(button_delay)


  if (buttons & cwiid.BTN_DOWN):
    print 'Down pressed'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_1):
    print 'Button 1 pressed'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_2):
    print 'Button 2 pressed'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_A):
    print 'Button A pressed'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_B):
    print 'Button B pressed'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_HOME):
    wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
    check = 0
    while check == 0:
      print(wii.state['acc'])
      time.sleep(0.01)
      check = (buttons & cwiid.BTN_HOME)
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_MINUS):
    print 'Minus Button pressed'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_PLUS):
    print 'Plus Button pressed'
    time.sleep(button_delay)
