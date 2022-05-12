from djitellopy import tello
from time import sleep

tello = tello.Tello()

#Starting up
tello.connect()
print(tello.get_battery())
tello.takeoff()
tello.move_up(120)
sleep(0.2)

#Moving Forward
tello.move_forward(400)
tello.rotate_counter_clockwise(90)

#Rotating across the Room
tello.move_forward(400)
sleep(0.1)
tello.rotate_clockwise(90)
sleep(0.1)
tello.move_forward(400)
sleep(1)

#Moving Back to the other Side
tello.flip_back()
sleep(0.1)
tello.move_back(500)
tello.move_back(300)

#Landing
tello.rotate_clockwise(90)
sleep(0.1)
tello.move_forward(400)
sleep(1)
tello.land()
sleep(1)
tello.land()
