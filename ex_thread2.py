import RPi.GPIO as GPIO 
import time
import threading

GPIO.setmode(GPIO.BCM)

#Pull_down 저항 이용 : 스위치 연결 (1) 3.3V (2)연결핀  
  
class LedControl : 
    def __init__(self, sw1, led_pins):
        GPIO.setmode(GPIO.BCM) 
        self.sw1 = sw1 
        GPIO.setup(self.sw1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self.led_pins = led_pins 
        self.new_sw = GPIO.input(self.sw1) 
        self.old_sw = 0 
        self.count = 0
        self.pin = 0

        for self.pin in self.led_pins : 
            GPIO.setup(self.pin, GPIO.OUT, initial=GPIO.LOW) 

    def up_led(self): 
        while True : 
            self.new_sw = GPIO.input(self.sw1)
            if self.new_sw != self.old_sw:
                self.old_sw = self.new_sw
                if self.new_sw == 1: 
                    print('Status SW', GPIO.input(self.sw1)) 
                    print(self.count)
                    GPIO.output(self.led_pins[self.count], GPIO.HIGH)
                    time.sleep(1)
                    GPIO.output(self.led_pins[self.count], GPIO.LOW)
                    if self.count == 2 : 
                        self.count = 0
                    else :
                        self.count += 1
        
class LedControl_down(LedControl): 
    def __init__(self, sw1, led_pins):
       super().__init__(sw1, led_pins)
                

    def down_led(self): 
        while True :
            self.new_sw = GPIO.input(self.sw1)
            if self.new_sw != self.old_sw:
                self.old_sw = self.new_sw
                if self.new_sw == 1: 
                    print('Status SW', GPIO.input(self.sw1)) 
                    print(self.count)
                    GPIO.output(self.led_pins[self.count], GPIO.HIGH)
                    time.sleep(1)
                    GPIO.output(self.led_pins[self.count], GPIO.LOW)
                    if self.count == 0 : 
                        self.count = 2
                    else :
                        self.count -= 1

if __name__ == '__main__': 

    sw1 = 25
    sw2 = 8

    led_pins = [18, 23, 24]    
    
    led_control1 = LedControl(sw1, led_pins) 
    led_control2 = LedControl_down(sw2, led_pins) 

    sw_up_threading=threading.Thread(target=led_control1.up_led) 
    sw_up_threading.start() 
       
    sw_down_threading=threading.Thread(target=led_control2.down_led) 
    sw_down_threading.start()

    try : 
        while True: 
            print('Waiting SW1 or SW2') 

    except KeyboardInterrupt: 
        pass 

    finally : 
        GPIO.cleanup() 


