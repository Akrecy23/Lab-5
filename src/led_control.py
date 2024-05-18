from hal import hal_led as led
from threading import Thread
from time import sleep

from hal import hal_keypad as keypad

def main():
    #Initialise led
    led.init()
    led_control_init()

def led_thread():
    global delay

    delay = 0

    while(True):
        if delay != 0:
            led.set_output(24,1) #set led high
            sleep(delay) #led high for "delay" seconds
            led.set_output(24,0) #set led low
            sleep(delay) #led low for "delay" seconds

def led_control_init():
    
    global delay
    t1 = Thread(target=led_thread)
    t1.start() 
    delay = 1 #Set initial LED blinking every 1 second after Thread starts

def set_delay(new_delay):
    global delay
    delay = new_delay

if __name__ == "__main__":
    main()