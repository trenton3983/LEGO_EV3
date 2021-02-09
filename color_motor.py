#!/usr/bin/env python3

# Drive Forward and Stop at Pure Green Line

# Import methods from modules
from time import sleep
from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sound import Sound

sound = Sound()
sound.speak('Commence testing of program for Sam')
sound.speak('Drive forward and stop at green line')

# create an object for the color sensor on input 2
colorLeft = ColorSensor(INPUT_2)

# create an object for the motors on output b and c
steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)

# set the direction for straight
direction = 0

# turn the motors on at speed 20
steering_drive.on(direction, 20)

# continuously check the color until the sensor detects pure green
while True:
    if colorLeft.rgb[0] < 60 and colorLeft.rgb[1] > 75 and colorLeft.rgb[2] < 40:
        print('Left RGB: ' + str(colorLeft.rgb))
        sleep(0.01)

        # Explicitly stop motors at end of program
        steering_drive.off()
        break

sleep(3)

sound.speak('Commence drawing a regular pentagon')

for x in range(5):
    steering_drive.on_for_seconds(steering=0, speed=20, seconds=3)
    steering_drive.on_for_degrees(steering=-100, speed=20, degrees=160)
steering_drive.off()