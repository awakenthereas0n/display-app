#!/usr/bin/python

import sys
import time
from Quartz.CoreGraphics import *
def mouseEvent(type, posx, posy):
        theEvent = CGEventCreateMouseEvent(None, type, (posx,posy), kCGMouseButtonLeft)
        CGEventPost(kCGHIDEventTap, theEvent)
def mousemove(posx,posy):
        mouseEvent(kCGEventMouseMoved, posx,posy);
def mouseclick(posx,posy):
        mouseEvent(kCGEventLeftMouseDown, posx,posy);
        mouseEvent(kCGEventLeftMouseUp, posx,posy);
ourEvent = CGEventCreate(None); 
# Save current mouse position
currentpos=CGEventGetLocation(ourEvent); 
# Click the "Apple" 
mouseclick(25, 5);   
# 1 second delay        
time.sleep(1);         
# Restore mouse position 
mousemove(int(currentpos.x),int(currentpos.y))