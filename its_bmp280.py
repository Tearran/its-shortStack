#!/usr/bin/env python3

from lib.bmp_280 import BMP280
from time import sleep

bmp = BMP280(port=1, mode=BMP280.FORCED_MODE, oversampling_p=BMP280.OVERSAMPLING_P_x16, oversampling_t=BMP280.OVERSAMPLING_T_x1,filter=BMP280.IIR_FILTER_OFF, standby=BMP280.T_STANDBY_1000)

pressure = bmp.read_pressure() 
temp = bmp.read_temperature()
tempf = temp * 1.8 + 32 

pressure = str(round(pressure,2 ))
temp = str(round(temp, 2))
tempf = str(round(tempf, 1 ))

print(pressure + " hPa: ")
print(tempf + " °F: ")
print(temp + " °C: ")
