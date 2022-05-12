from djitellopy import tello
from time import sleep

me = tello.Tello()

print(me.get_battery())

#Starting up
tello.connect()
tello.takeoff(120)
sleep(0.2)

#Moving Forward
tello.move_forward(400)
tello.rotatecounterclockwise(90)

#Rotating across the Room
tello.move_forward(400)
tello.rotateclockwise(90)
tello.move_forward(400)
sleep(1)

#Moving Back to the other Side
tello.flip_backwards(tello)
tello.move_backwards(850)

#Landing
tello.rotateclockwise(90)
tello.moveforward(400)
sleep(1)
tello.land()
