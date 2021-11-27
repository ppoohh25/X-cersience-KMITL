from machine import Pin
from utime import sleep
# A
# ---
# F | G | B
# ---
# E | | C
# ---
# D
A = Pin(2,Pin.OUT) # A
B = Pin(3,Pin.OUT) # B
C = Pin(4,Pin.OUT) # C
D = Pin(5,Pin.OUT) # D
E = Pin(6,Pin.OUT) # E
F = Pin(8,Pin.OUT) # F
G = Pin(7,Pin.OUT) # G
while True:
    D.on()
    sleep(1)