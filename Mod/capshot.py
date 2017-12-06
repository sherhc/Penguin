#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import ImageGrab  # pip install pillow

def get_shot(pic_name):
	from ctypes import windll
	user32 = windll.user32
	user32.SetProcessDPIAware()
	pic=ImageGrab.grab()
	pic.save(pic_name)
	
def get_cams(pic_name):
	from VideoCapture import Device
	cam = Device(devnum=0, showVideoWindow=0)
	cam.saveSnapshot(pic_name,quality=100,timestamp=3, boldfont=1)
	
def get_video():
	pass