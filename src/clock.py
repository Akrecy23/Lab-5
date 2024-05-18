import time
from threading import Thread
from hal import hal_lcd as LCD

lcd = LCD.lcd()

def get_time(not_blink):
    local_time = time.localtime() #get struct_time

    if not_blink == True:
        time_string = time.strftime("%H:%M:%S", local_time)
    else:
        time_string = time.strftime("%H %M %S", local_time) #Replace colons with space if blinking

    return time_string

def get_date():
    local_time = time.localtime() #get struct_time
    date_string = time.strftime("%d:%m:%Y", local_time)
    return date_string

def display_time():

    not_blink = True
    
    while (1):
        time_string = get_time(not_blink)
        date_string = get_date()
        lcd.lcd_display_string(time_string, 1)
        lcd.lcd_display_string(date_string, 2)

        not_blink = not not_blink #Is blinking

        time.sleep(1)

def init_all():
    lcd = LCD.lcd()
    lcd.lcd_clear()

    display_thread = Thread(target=display_time)
    display_thread.start()

def main():
    init_all()
    

if __name__ == "__main__":
    main()