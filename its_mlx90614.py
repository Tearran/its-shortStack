#!/usr/bin/env python3

from lib.mlx90614 import MLX90614
import sys

thermometer_address = 0x5a
thermometer = MLX90614(thermometer_address)
#print(str(round(thermometer.get_amb_temp() * 1.8 + 32, 1)))
#print(str(round(thermometer.get_obj_temp()* 1.8 + 32, 1)))
print(str(thermometer.get_amb_temp()))
print(str(thermometer.get_obj_temp()))