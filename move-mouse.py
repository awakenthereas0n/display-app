#!/usr/bin/python

import time
from Quartz.CoreGraphics import *
def mouseEvent(type, posx, posy):
           theEvent = CGEventCreateMouseEvent(None, type, (posx,posy), kCGMouseButtonLeft)
           CGEventPost(kCGHIDEventTap, theEvent)
def mousemove(posx,posy):
           mouseEvent(kCGEventMouseMoved, posx,posy);
def mouseclickdn(posx,posy):
           mouseEvent(kCGEventLeftMouseDown, posx,posy);
def mouseclickup(posx,posy):
           mouseEvent(kCGEventLeftMouseUp, posx,posy);
def mousedrag(posx,posy):
           mouseEvent(kCGEventLeftMouseDragged, posx,posy);
ourEvent = CGEventCreate(None); 
# Save current mouse position
currentpos=CGEventGetLocation(ourEvent); 
# move mouse to upper left of screen
mouseclickdn(40, 60);
# drag icon to new location
mousedrag(60, 300);
# release mouse
mouseclickup(60, 300);
# necessary delay
time.sleep(1);
# return mouse to start positon
mouseclickdn(int(currentpos.x),int(currentpos.y));