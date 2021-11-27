from machine import Pin
import utime

led = Pin(2,Pin.OUT)

while True:
    led.on()
    utime.sleep(0.2)
    led.off()
    utime.sleep(0.2)
