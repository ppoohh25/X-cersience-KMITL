import machine
import utime
from machine import Pin

led = Pin(2,Pin.OUT)
temp = machine.ADC(28)

while True:
  temp_read = temp.read_u16()
  print(temp_read)

  if(temp_read < 30000):
    led.on()
    print('led on')
  else:
    led.off()
    print('led off')
 
  utime.sleep(1)
