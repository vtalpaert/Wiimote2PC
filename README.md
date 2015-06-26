Wiimote to linux
=======

Script to connect Wiimote to linux, then PC sends motion commands to robot (two PWM factors, todo).


Example is with the turtle package, try 'python wiimote-PC.py' in your terminal.
You can either use the arrows to steer, B to accelerate and A to decelerate. + and - turn on itself.
Or you can press HOME and control through wiimote position: pointing up is still, point forward to move forward and to the sides to turn.

NOTE: We assume we can ignore the accelerations of moving the Wiimote because of how slow we move, so the position is related to gravity.
