import machine
import utime

temp = machine.ADC(26)

while True:
    temp_read = temp.read_u16()
    print(temp_read)
    utime.sleep(1)