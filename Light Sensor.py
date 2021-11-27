from machine import ADC
from utime import sleep

ldr = machine.ADC(26)

while True:
    ldr_read = ldr.read_u16()
    print(ldr_read)
    utime.sleep(1)