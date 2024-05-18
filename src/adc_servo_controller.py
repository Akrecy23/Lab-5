from hal import hal_adc as adc
from hal import hal_servo as servo
from threading import Thread

import RPi.GPIO as GPIO
from time import sleep

def main():
    #Initialise adc
    adc.init()
    data = adc.get_adc_value(1) #Data is value from 0-1023

    servo_pos = -60/341 * data + 180 #y=mx+c

    #Initialise servo motor
    servo.init()
    servo.set_servo_position(servo_pos)

if __name__ == "__main__":
    main()