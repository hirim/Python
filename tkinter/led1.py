import RPi.GPIO as GPIO
import time
import tkinter as tk

app = tk.Tk()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

app.title(‘Dimming Control System of LED’)
app.geometry(‘400x400’)

led1 = 20
GPIO.setup(led1, GPIO.OUT)
p = GPIO.PWM(led1, 50)
p.start(0)

def light_on():
    for dc in range(1, 101, 5):
        p.ChangeDutyCycle(dc)
        time.sleep(0.2)

def light_off():
    for dc in range(100, -1, -5):
        p.ChangeDutyCycle(dc)
        time.sleep(0.2)

def exit_but():
    GPIO.cleanup()
    exit()

but1 = tk.Button(app, text = ‘on’, command = light_on)
but1.grid(row=1, column =1)
but2 = tk.Button(app, text = ‘off’, command = light_off)
but2.grid(row=1, column=2)
but3 = tk.Button(app, text = ‘exit’, command = exit_but)
but3.grid(row=1, column=2)

app.mainloop()
