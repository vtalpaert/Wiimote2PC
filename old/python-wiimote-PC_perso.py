#############################

# Unfinished
# This code is a fail. It does work as the original code but is not an improvement (maybe in speed, but that is not the issue). Indeed pressing UP and LEFT will be easy to detect (sum of values), but if an additional button is pressed this does not work anymore.
# I could try to predict the results between two values by inspecting the different possibilities, only they are millions of combinations minus the permutations, etc... sum of Newton's binomes ^^


# Solution: more if statements in the original code...


#############################














# This program utilises the cwiid Python library in order to get input over bluetooth from a wiimote.
# Coded by The Raspberry Pi Guy. Work based on some of Matt Hawkins's!

# Modified by Victor Talpaert, June 2015.
# The aim is to react to some buttons combinations

import cwiid, time, switch


button_delay = 0.1

# dictionnary - button mapping
B2 = 1 # Button 2
B1 = 2 # Button 1
TRIGGERB = 4
A = 8
MINUS = 16
HOME = 128
LEFT = 256
RIGHT = 512
DOWN = 1024
UP = 2048
PLUS = 4096


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

  for case in switch.switch(buttons):
    if case(B2):
        print 'Button 2 pressed'
    	time.sleep(button_delay)
        break

    if case(B1):
        print 'Button 1 pressed'
    	time.sleep(button_delay)
        break

    if case(TRIGGERB):
        print 10
        break

    if case(A):
        print 11
        break

    if case(MINUS):
        print 11
        break

    if case(HOME):
        print 11
        break

    if case(LEFT):
 	print 'Left pressed'
    	time.sleep(button_delay)
        break

    if case(RIGHT):
        print 'Right pressed'
    	time.sleep(button_delay)
        break

    if case(DOWN):
        print 'Down pressed'
    	time.sleep(button_delay)
        break

    if case(UP):
        print 'Up pressed'
    	time.sleep(button_delay)
        break

    if case(PLUS):
        print 11
        break

#    if case(): # default, could also just omit condition or 'if True'
#        print "something else!"
        # No need to break here, it'll stop anyway

# break is used here to look as much like the real thing as possible, but
# elif is generally just as good and more concise.




  # Detects whether + and - are held down and if they are it quits the program
  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
    print '\nClosing connection ...'
    # NOTE: This is how you RUMBLE the Wiimote
    wii.rumble = 1
    time.sleep(0.1)
    wii.rumble = 0
    exit(wii)

  # The following code detects whether any of the Wiimotes buttons have been pressed and then prints a statement to the screen!

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
