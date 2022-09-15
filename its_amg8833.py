#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from lib.amg8833 import AMGGridEye

# ini amg8833 lib
sensor = AMGGridEye()
sensor.reset_flags_and_settings()
time.sleep(.1)
sensor.set_fps_mode(AMGGridEye.FPS_10_MODE)

try:  
#while(True):
  #update temperature
  sensor.update_pixel_temperature_matrix()
  time.sleep(.1)
  
finally:
  print(sensor.get_pixel_temperature_matrix())
  #print(str(round(sensor.get_thermistor_temperature(), 0))) 
