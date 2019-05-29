#!/usr/bin/env python
"""步进电机控制.
接线方式：IN1接PIN38(PG6) IN2接PIN40(PG7) IN3接PIN32(PG8) IN4接PIN36(PG9) 
          VCC接 5v GND接Ground
"""

import os
import sys
import time

if not os.getegid() == 0:
    sys.exit('Script must be run as root')


from pyA20.gpio import gpio
from pyA20.gpio import connector
from pyA20.gpio import port

__author__ = "Stefan Mavrodiev"
__copyright__ = "Copyright 2014, Olimex LTD"
__credits__ = ["Stefan Mavrodiev"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = __author__
__email__ = "support@olimex.com"

def stepmotor():
#初始化gpio端口
    gpio.init()
    in1 = connector.gpio1p38
    in2 = connector.gpio1p40
    in3 = connector.gpio1p32
    in4 = connector.gpio1p36

    steps = 130
    clockwise = 1

    arr = [0,1,2,3];
    if clockwise!=1:
       arr = [3,2,1,0]

    ports = [in1,in2,in3,in4]              # Pin38 Pin40 Pin32 Pin36
 
    for p in ports:
        gpio.setcfg(p,gpio.OUTPUT)
    
    for x in range(0,steps):
        for j in arr:
            time.sleep(0.005)
            for i in range(0,4):
                if i == j:
                   gpio.output(ports[i],True)
                else:
                   gpio.output(ports[i],False)

if __name__ == '__main__':

     stepmotor()




################################
#作者：hpzweb
#来源:原创作品

